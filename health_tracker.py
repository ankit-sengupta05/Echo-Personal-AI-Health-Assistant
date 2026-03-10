"""
Echo Health Assistant - Health Tracker
Handles medication lookup, diet plans, and session history
"""

import pandas as pd
import os
from datetime import datetime


class HealthTracker:
    def __init__(self, med_path="data/medications.csv", diet_path="data/diet_plans.csv"):
        self.med_path = med_path
        self.diet_path = diet_path
        self.med_df = None
        self.diet_df = None
        self.session_history = []  # Stores past queries this session
        self._load_data()

    def _load_data(self):
        """Load medication and diet CSV datasets."""
        base = os.path.dirname(os.path.abspath(__file__))
        try:
            med_full = os.path.join(base, self.med_path)
            self.med_df = pd.read_csv(med_full)
            print(f"[HealthTracker] Loaded {len(self.med_df)} medication records.")
        except Exception as e:
            print(f"[HealthTracker] Error loading medications: {e}")
            self.med_df = pd.DataFrame()

        try:
            diet_full = os.path.join(base, self.diet_path)
            self.diet_df = pd.read_csv(diet_full)
            print(f"[HealthTracker] Loaded {len(self.diet_df)} diet plan records.")
        except Exception as e:
            print(f"[HealthTracker] Error loading diet plans: {e}")
            self.diet_df = pd.DataFrame()

    def get_medications(self, disease):
        """Return structured medication info for a disease."""
        if self.med_df is None or self.med_df.empty:
            return None

        row = self.med_df[self.med_df["disease"].str.lower() == disease.lower()]
        if row.empty:
            return None

        r = row.iloc[0]
        meds = []
        for i in range(1, 4):
            med_name = str(r.get(f"medication{i}", "")).strip()
            dosage = str(r.get(f"dosage{i}", "")).strip()
            if med_name and med_name.lower() != "nan":
                meds.append({"name": med_name, "dosage": dosage})

        return {
            "disease": disease,
            "medications": meds,
            "precautions": str(r.get("precautions", "")).strip(),
            "otc": str(r.get("otc", "Unknown")).strip()
        }

    def get_diet_plan(self, disease):
        """Return structured diet plan for a disease."""
        if self.diet_df is None or self.diet_df.empty:
            return None

        row = self.diet_df[self.diet_df["disease"].str.lower() == disease.lower()]
        if row.empty:
            return None

        r = row.iloc[0]
        return {
            "disease": disease,
            "foods_to_eat": str(r.get("foods_to_eat", "")).strip(),
            "foods_to_avoid": str(r.get("foods_to_avoid", "")).strip(),
            "meal_plan": str(r.get("meal_plan", "")).strip(),
            "hydration": str(r.get("hydration", "")).strip(),
            "supplements": str(r.get("supplements", "")).strip()
        }

    def log_session(self, symptoms_input, results):
        """Log a symptom check to the session history."""
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "symptoms": symptoms_input.strip(),
            "top_result": results[0]["disease"] if results else "No match",
            "confidence": results[0]["confidence"] if results else 0
        }
        self.session_history.append(entry)
        return entry

    def get_session_history(self):
        """Return all session history entries."""
        return self.session_history

    def clear_history(self):
        """Clear all session history."""
        self.session_history = []

    def get_full_report(self, disease):
        """Return combined medication + diet report for a disease."""
        meds = self.get_medications(disease)
        diet = self.get_diet_plan(disease)
        return {"medications": meds, "diet": diet}

    def format_medication_text(self, disease):
        """Return formatted plain-text medication summary."""
        data = self.get_medications(disease)
        if not data:
            return f"No medication data found for {disease}."

        lines = [f"💊 MEDICATIONS FOR {disease.upper()}", ""]
        for i, med in enumerate(data["medications"], 1):
            lines.append(f"  {i}. {med['name']}")
            lines.append(f"     Dosage: {med['dosage']}")
            lines.append("")

        otc_label = "✅ OTC Available" if data["otc"].lower() == "yes" else (
            "⚠️ Partial OTC" if "partial" in data["otc"].lower() else "🔒 Prescription Only"
        )
        lines.append(f"  Availability: {otc_label}")
        lines.append("")
        lines.append(f"  ⚠️ Precautions: {data['precautions']}")
        lines.append(f"  {data['precautions']}")
        lines.append("")
        lines.append("  ⚕️ Always consult a licensed doctor before starting any medication.")

        return "\n".join(lines)

    def format_diet_text(self, disease):
        """Return formatted plain-text diet plan summary."""
        data = self.get_diet_plan(disease)
        if not data:
            return f"No diet plan found for {disease}."

        lines = [f"🥗 DIET PLAN FOR {disease.upper()}", ""]
        lines.append("  ✅ Foods to Eat:")
        lines.append(f"  {data['foods_to_eat']}")
        lines.append("")
        lines.append("  ❌ Foods to Avoid:")
        lines.append(f"  {data['foods_to_avoid']}")
        lines.append("")
        lines.append("  🍽️ Sample Meal Plan:")
        lines.append(f"  {data['meal_plan']}")
        lines.append("")
        lines.append("  💧 Hydration:")
        lines.append(f"  {data['hydration']}")
        lines.append("")
        lines.append("  💊 Recommended Supplements:")
        lines.append(f"  {data['supplements']}")

        return "\n".join(lines)
