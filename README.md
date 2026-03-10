<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=200&section=header&text=💊%20Echo&fontSize=80&fontColor=00D9C0&animation=fadeIn&fontAlignY=35&desc=Personal%20AI%20Health%20Assistant&descAlignY=58&descColor=8B949E&descSize=22" width="100%"/>

<!-- Typing Animation -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=00D9C0&center=true&vCenter=true&width=700&lines=AI-Powered+Symptom+Checker;Fuzzy+Logic+Disease+Matching;Personalised+Medication+Guide;Smart+Diet+%26+Nutrition+Plans;Your+Personal+Health+Companion+🩺" alt="Typing SVG" />
</a>

<br/>

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-00D9C0?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/library/tkinter.html)
[![FuzzyWuzzy](https://img.shields.io/badge/FuzzyWuzzy-AI%20Matching-BC8CFF?style=for-the-badge&logo=buffer&logoColor=white)](https://github.com/seatgeek/fuzzywuzzy)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Engine-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-3FB950?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Mac%20%7C%20Linux-58A6FF?style=for-the-badge&logo=windows&logoColor=white)]()
[![Diseases](https://img.shields.io/badge/Dataset-20%20Diseases-F85149?style=for-the-badge&logo=databricks&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Active-00D9C0?style=for-the-badge&logo=statuspage&logoColor=white)]()

<br/>

> **⚕️ Disclaimer:** Echo is an educational AI tool. It does **not** replace professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.

</div>

---

## 🧬 What is Echo?

**Echo** is a desktop AI health assistant built with Python and Tkinter that helps users identify possible health conditions based on their symptoms using **fuzzy logic matching**. It provides personalised medication guides, diet plans, and tracks your session history — all from a clean, dark-themed GUI powered by CSV datasets.

```
User enters symptoms  →  FuzzyWuzzy AI matches  →  Top diseases ranked by confidence
        ↓                                                       ↓
  Session logged    ←   Diet Plan loaded       ←   Medications displayed
```

---

## ✨ Features at a Glance

<table>
<tr>
<td width="50%">

### 🔍 Symptom Intelligence
- Fuzzy logic matching via **FuzzyWuzzy**
- Handles **typos, partial words, synonyms**
- Adjustable sensitivity threshold (40–90%)
- Confidence score per disease match
- Top 5 ranked results with visual bars

</td>
<td width="50%">

### 💊 Medication Guide
- 3 medications per condition with dosages
- OTC vs Prescription classification
- Important precautions & warnings
- Auto-loaded from symptom results
- Covers **20 diseases** in the dataset

</td>
</tr>
<tr>
<td width="50%">

### 🥗 Diet & Nutrition
- Foods to eat AND foods to avoid
- Personalised sample **meal plans**
- Daily hydration recommendations
- Supplement & vitamin suggestions
- Based on clinical nutritional guidelines

</td>
<td width="50%">

### 📋 Session History
- Timestamped symptom check logs
- Top match + confidence recorded
- Full session review in one view
- One-click history clear
- Lightweight in-memory storage

</td>
</tr>
</table>

---

## 🗂️ Project Structure

```
📦 echo_health_assistant/
│
├── 🚀 main.py                ← Entry point — run this
├── 🖥️  app.py                ← Main Tkinter GUI (4 tabs)
├── 🧠 symptom_engine.py      ← FuzzyWuzzy matching logic
├── 💾 health_tracker.py      ← Medication & diet + history
├── 🎨 ui_components.py       ← Custom dark-theme widgets
├── 📄 requirements.txt
│
└── 📂 data/
    ├── 🗃️  symptoms.csv       ← 20 diseases × 6 symptoms each
    ├── 💊 medications.csv    ← 3 meds + dosages per disease
    └── 🥗 diet_plans.csv     ← Full diet + supplement plans
```

---

## 🖥️ GUI Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  💊 Echo — Personal AI Health Assistant       [FuzzyWuzzy AI]   │
├──────────────────┬────────────────┬───────────┬─────────────────┤
│  🔍 Symptom      │ 💊 Medications  │ 🥗 Diet   │  📋 History     │
│  Checker         │ Guide          │ Plans     │                 │
├──────────────────┴────────────────┴───────────┴─────────────────┤
│                                                                  │
│  ┌─────────────────────┐   ┌──────────────────────────────────┐ │
│  │ Describe Symptoms   │   │ Analysis Results                 │ │
│  │ ┌─────────────────┐ │   │  #1 ██████████████░░ 87.4%      │ │
│  │ │ headache, fever,│ │   │  #2 ████████░░░░░░░░ 61.2%      │ │
│  │ │ nausea...       │ │   │  #3 █████░░░░░░░░░░░ 43.8%      │ │
│  │ └─────────────────┘ │   │                                  │ │
│  │ Sensitivity: [60%]  │   │  🏆 Most Likely: Influenza       │ │
│  │ [🔍 Analyze] [✖]   │   │  Confidence: 87.4%               │ │
│  └─────────────────────┘   └──────────────────────────────────┘ │
│                                                                  │
│  ⚕️ Not a substitute for professional medical advice             │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚙️ How the AI Matching Works

```
                    ┌─────────────────────────────┐
                    │   User Input (raw text)      │
                    │   "headache, fevr, nausea"   │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   Tokenize & Normalize       │
                    │   Split by comma / newline   │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   FuzzyWuzzy Matching        │
                    │   token_sort_ratio per sym   │
                    │   "fevr"  → "fever"  (94%)   │
                    │   "headach"→"headache"(91%)  │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   Disease Scoring Formula    │
                    │                              │
                    │   Score = (FuzzyQ × 0.6)     │
                    │         + (Coverage × 0.4)   │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │   Top 5 Ranked Results       │
                    │   + Visual Confidence Bars   │
                    └─────────────────────────────┘
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python **3.8 or higher**
- pip package manager
- Windows / macOS / Linux

### Step-by-Step Commands

```bash
# 1️⃣  Navigate to project folder
cd echo_health_assistant

# 2️⃣  Create a virtual environment
python -m venv venv

# 3️⃣  Activate venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac / Linux

# 4️⃣  Install dependencies
pip install fuzzywuzzy python-Levenshtein pandas Pillow

# 5️⃣  Launch Echo
python main.py
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---|---|---|
| `fuzzywuzzy` | 0.18.0 | Fuzzy string matching for symptoms |
| `python-Levenshtein` | 0.21.1 | Speeds up FuzzyWuzzy by 4–10× |
| `pandas` | 2.1.4 | CSV dataset loading & querying |
| `Pillow` | 10.2.0 | Image support for Tkinter |
| `tkinter` | built-in | GUI framework (no install needed) |

---

## 🩺 Supported Conditions (20 Diseases)

<table>
<tr><td>🤧 Common Cold</td><td>🤒 Influenza</td><td>🦠 COVID-19</td><td>🤕 Migraine</td></tr>
<tr><td>❤️ Hypertension</td><td>🍬 Diabetes Type 2</td><td>💨 Asthma</td><td>🩸 Anemia</td></tr>
<tr><td>🫀 Gastritis</td><td>😰 Anxiety Disorder</td><td>😔 Depression</td><td>🦠 UTI</td></tr>
<tr><td>🦴 Arthritis</td><td>🦋 Thyroid Disorder</td><td>🦟 Dengue Fever</td><td>🫁 Pneumonia</td></tr>
<tr><td>🫃 IBS</td><td>🧴 Eczema</td><td>👃 Sinusitis</td><td>🪨 Kidney Stones</td></tr>
</table>

---

## 🔑 Key Technical Points

- **Fuzzy Matching:** Uses `fuzz.token_sort_ratio` — handles typos, word-order variations, and partial matches perfectly for medical symptom text
- **Confidence Formula:** Weighted blend: 60% fuzzy quality + 40% symptom coverage ratio — avoids false positives from single-symptom hits
- **Threading:** Symptom analysis runs on a background thread so the GUI stays fully responsive during processing
- **CSV Architecture:** All disease data in plain CSV — extend the dataset by simply adding rows, zero code changes required
- **Rich Text Tags:** Tkinter `Text` widget uses named tags (`heading`, `success`, `warning`) for coloured output — requires `foreground=` not `fg=` in `tag_configure`
- **Auto-fill Tabs:** After analysis, Medications and Diet tabs automatically pre-load data for the top-matched disease
- **Session Logging:** Every symptom check is timestamped and stored in-memory, visible in the History tab

---

## 🐛 Common Error & Fix

### `bitmap "#00D9C0" not defined`

```
_tkinter.TclError: bitmap "#00D9C0" not defined
```

**Root Cause:** Tkinter's `Text.tag_configure()` does **not** accept `fg=` — it requires `foreground=`

```python
# ❌ WRONG — causes TclError on all platforms
self.text.tag_configure("heading", fg="#00D9C0", font=...)

# ✅ CORRECT — use foreground= for Text widget tags
self.text.tag_configure("heading", foreground="#00D9C0", font=...)
```

This fix is already applied in the latest `ui_components.py`.

---

## 🗺️ Architecture Flow

```
┌─────────────┐     ┌──────────────────┐     ┌────────────────────┐
│  main.py    │────▶│   EchoApp()      │────▶│  4 Notebook Tabs   │
│  Entry Point│     │   app.py         │     │  Symptom / Med /   │
└─────────────┘     └────────┬─────────┘     │  Diet / History    │
                              │               └────────────────────┘
               ┌──────────────┼──────────────┐
               ▼              ▼              ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐
    │ symptom_     │  │ health_      │  │  ui_components.py    │
    │ engine.py    │  │ tracker.py   │  │  CardFrame           │
    │              │  │              │  │  EchoButton          │
    │ FuzzyWuzzy   │  │ Medications  │  │  ScrollText          │
    │ Scoring      │  │ Diet Plans   │  │  ConfidenceBar       │
    │ Ranking      │  │ History Log  │  │  TagEntry / Badge    │
    └──────┬───────┘  └──────┬───────┘  └──────────────────────┘
           │                 │
           └────────┬────────┘
                    ▼
         ┌─────────────────────┐
         │      data/          │
         │  symptoms.csv       │
         │  medications.csv    │
         │  diet_plans.csv     │
         └─────────────────────┘
```

---

## 🤝 Contributing

1. **Fork** the repository
2. **Branch:** `git checkout -b feature/add-more-diseases`
3. **Extend** CSV files with new diseases
4. **Commit:** `git commit -m "Add 10 more diseases to dataset"`
5. Open a **Pull Request**

### Ideas Welcome
- More diseases & symptoms in CSV
- BMI / vitals calculator tab
- PDF report export
- Voice symptom input
- Real medical API integration (e.g. OpenFDA)

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=120&section=footer&animation=fadeIn" width="100%"/>

**Built with 💊 by the Echo Team**

*Empowering people with health awareness — not replacing doctors*

</div>
