"""
Echo Health Assistant - Symptom Matching Engine
Uses FuzzyWuzzy for intelligent symptom-to-disease matching
"""

import os
import pandas as pd
from fuzzywuzzy import fuzz, process


class SymptomEngine:
    def __init__(self, data_path="data/symptoms.csv"):
        self.data_path = data_path
        self.df = None
        self.symptom_columns = []
        self.all_symptoms = []
        self.symptom_disease_map = {}
        self._load_data()

    def _load_data(self):
        try:
            base = os.path.dirname(os.path.abspath(__file__))
            path = os.path.join(base, self.data_path)
            self.df = pd.read_csv(path)
            self.symptom_columns = [col for col in self.df.columns if col.startswith("symptom")]

            for _, row in self.df.iterrows():
                disease = row["disease"]
                for col in self.symptom_columns:
                    symptom = str(row[col]).strip().lower()
                    if symptom and symptom != "nan":
                        self.symptom_disease_map.setdefault(symptom, []).append(disease)
                        self.all_symptoms.append(symptom)

            self.all_symptoms = list(set(self.all_symptoms))
            print(
                f"[SymptomEngine] Loaded {len(self.df)} diseases, "
                f"{len(self.all_symptoms)} unique symptoms."
            )
        except Exception as e:
            print(f"[SymptomEngine] Error loading data: {e}")
            self.df = pd.DataFrame()

    def fuzzy_match_symptom(self, user_input, threshold=60):
        user_input = user_input.strip().lower()
        if not user_input or not self.all_symptoms:
            return []

        matches = process.extractBests(
            user_input,
            self.all_symptoms,
            scorer=fuzz.token_sort_ratio,
            score_cutoff=threshold,
            limit=5,
        )
        return [(match, score) for match, score in matches]

    def analyze_symptoms(self, user_symptoms_text, threshold=60):
        if not user_symptoms_text.strip():
            return []

        raw = [
            s.strip().lower()
            for s in user_symptoms_text.replace("\n", ",").split(",")
            if s.strip()
        ]

        matched_symptoms = {}
        for user_sym in raw:
            matches = self.fuzzy_match_symptom(user_sym, threshold)
            for matched_sym, score in matches:
                if matched_sym not in matched_symptoms or matched_symptoms[matched_sym] < score:
                    matched_symptoms[matched_sym] = score

        if not matched_symptoms:
            return []

        disease_scores = {}
        disease_symptom_matches = {}

        for _, row in self.df.iterrows():
            disease = row["disease"]
            disease_syms = [
                str(row[col]).strip().lower()
                for col in self.symptom_columns
                if str(row[col]).strip().lower() != "nan"
            ]
            total_syms = len(disease_syms)
            score_sum = 0
            hits = []

            for matched_sym, fuzzy_score in matched_symptoms.items():
                if matched_sym in disease_syms:
                    score_sum += fuzzy_score
                    hits.append(matched_sym)

            if hits:
                coverage = len(hits) / total_syms
                avg_fuzzy = score_sum / len(hits)
                confidence = round(avg_fuzzy * 0.6 + coverage * 100 * 0.4, 1)
                disease_scores[disease] = confidence
                disease_symptom_matches[disease] = hits

        sorted_results = sorted(disease_scores.items(), key=lambda x: x[1], reverse=True)

        results = []
        for disease, confidence in sorted_results[:5]:
            matched = disease_symptom_matches.get(disease, [])
            desc = self._get_description(disease)
            results.append(
                {
                    "disease": disease,
                    "confidence": confidence,
                    "matched_symptoms": matched,
                    "description": desc,
                }
            )
        return results

    def _get_description(self, disease):
        if self.df is not None and "description" in self.df.columns:
            row = self.df[self.df["disease"] == disease]
            if not row.empty:
                return row.iloc[0]["description"]
        return "No description available."

    def get_all_diseases(self):
        if self.df is not None:
            return self.df["disease"].tolist()
        return []

    def get_symptoms_for_disease(self, disease):
        if self.df is None:
            return []
        row = self.df[self.df["disease"] == disease]
        if row.empty:
            return []
        syms = []
        for col in self.symptom_columns:
            val = str(row.iloc[0][col]).strip()
            if val and val.lower() != "nan":
                syms.append(val)
        return syms
