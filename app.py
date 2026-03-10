"""
Echo Health Assistant - Main Application
Full-featured Tkinter GUI for AI-powered health analysis
"""

import tkinter as tk
from tkinter import ttk

from symptom_engine import SymptomEngine
from health_tracker import HealthTracker
from ui_components import (
    COLORS,
    FONTS,
    CardFrame,
    EchoButton,
    ScrollText,
    TagEntry,
    hsep,
    Badge,
)


class EchoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Echo — Personal AI Health Assistant")
        self.geometry("1100x780")
        self.minsize(900, 650)
        self.configure(bg=COLORS["bg_dark"])
        self.resizable(True, True)

        self.engine = SymptomEngine()
        self.tracker = HealthTracker()
        self.current_results = []

        self._setup_styles()
        self._build_ui()

    # ── Styles ───────────────────────────────────────────────────────────────
    def _setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "Echo.Vertical.TScrollbar",
            background=COLORS["bg_input"],
            troughcolor=COLORS["bg_panel"],
            arrowcolor=COLORS["text_muted"],
            borderwidth=0,
            width=8,
        )

        style.configure(
            "Echo.TNotebook",
            background=COLORS["bg_dark"],
            borderwidth=0,
            tabmargins=[0, 0, 0, 0],
        )

        style.configure(
            "Echo.TNotebook.Tab",
            background=COLORS["bg_panel"],
            foreground=COLORS["text_secondary"],
            font=FONTS["body"],
            padding=[18, 8],
            borderwidth=0,
        )

        style.map(
            "Echo.TNotebook.Tab",
            background=[("selected", COLORS["bg_card"])],
            foreground=[("selected", COLORS["accent_teal"])],
        )

    # ── UI Layout ─────────────────────────────────────────────────────────────
    def _build_ui(self):

        self._build_header()

        body = tk.Frame(self, bg=COLORS["bg_dark"])
        body.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        self.notebook = ttk.Notebook(body, style="Echo.TNotebook")
        self.notebook.pack(fill="both", expand=True)

        self.tab_symptoms = tk.Frame(self.notebook, bg=COLORS["bg_dark"])
        self.tab_medications = tk.Frame(self.notebook, bg=COLORS["bg_dark"])
        self.tab_diet = tk.Frame(self.notebook, bg=COLORS["bg_dark"])
        self.tab_history = tk.Frame(self.notebook, bg=COLORS["bg_dark"])

        self.notebook.add(self.tab_symptoms, text="🔍  Symptom Checker")
        self.notebook.add(self.tab_medications, text="💊  Medications")
        self.notebook.add(self.tab_diet, text="🥗  Diet Plans")
        self.notebook.add(self.tab_history, text="📋  History")

        self._build_symptom_tab()
        self._build_medication_tab()
        self._build_diet_tab()
        self._build_history_tab()

        self._build_statusbar()

    # ── Header ──────────────────────────────────────────────────────────────
    def _build_header(self):

        header = tk.Frame(self, bg=COLORS["bg_panel"], pady=12)
        header.pack(fill="x")

        inner = tk.Frame(header, bg=COLORS["bg_panel"])
        inner.pack(fill="x", padx=20)

        logo_frame = tk.Frame(inner, bg=COLORS["bg_panel"])
        logo_frame.pack(side="left")

        tk.Label(
            logo_frame,
            text="💊",
            font=("Segoe UI Emoji", 28),
            bg=COLORS["bg_panel"],
        ).pack(side="left", padx=(0, 10))

        title_stack = tk.Frame(logo_frame, bg=COLORS["bg_panel"])
        title_stack.pack(side="left")

        tk.Label(
            title_stack,
            text="Echo",
            font=FONTS["title"],
            fg=COLORS["accent_teal"],
            bg=COLORS["bg_panel"],
        ).pack(anchor="w")

        tk.Label(
            title_stack,
            text="Personal AI Health Assistant",
            font=FONTS["subtitle"],
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_panel"],
        ).pack(anchor="w")

        badge_frame = tk.Frame(inner, bg=COLORS["bg_panel"])
        badge_frame.pack(side="right")

        Badge(badge_frame, "FuzzyWuzzy AI", "info").pack(side="left", padx=4)
        Badge(badge_frame, "CSV Dataset", "purple").pack(side="left", padx=4)
        Badge(badge_frame, "20 Diseases", "success").pack(side="left", padx=4)

        tk.Frame(self, bg=COLORS["border"], height=1).pack(fill="x")

    # ── Status Bar ──────────────────────────────────────────────────────────
    def _build_statusbar(self):

        bar = tk.Frame(self, bg=COLORS["bg_panel"], pady=4)
        bar.pack(fill="x", side="bottom")

        self.status_var = tk.StringVar(
            value="Ready — Enter your symptoms to begin analysis"
        )

        tk.Label(
            bar,
            textvariable=self.status_var,
            font=FONTS["small"],
            fg=COLORS["text_muted"],
            bg=COLORS["bg_panel"],
        ).pack(side="left", padx=16)

        tk.Label(
            bar,
            text="⚕️ Not a substitute for professional medical advice",
            font=FONTS["small"],
            fg=COLORS["accent_red"],
            bg=COLORS["bg_panel"],
        ).pack(side="right", padx=16)

    # ── Symptom Tab ─────────────────────────────────────────────────────────
    def _build_symptom_tab(self):

        tab = self.tab_symptoms
        tab.columnconfigure(0, weight=2)
        tab.columnconfigure(1, weight=3)
        tab.rowconfigure(0, weight=1)

        left = tk.Frame(tab, bg=COLORS["bg_dark"])
        left.grid(row=0, column=0, sticky="nsew", padx=(8, 4), pady=8)

        input_card = CardFrame(
            left,
            title="Describe Your Symptoms",
            accent=COLORS["accent_teal"],
        )
        input_card.pack(fill="x", pady=(0, 8))

        tk.Label(
            input_card.content,
            text="Enter symptoms separated by commas or new lines:",
            font=FONTS["small"],
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_card"],
            wraplength=300,
            justify="left",
        ).pack(anchor="w", pady=(0, 6))

        self.symptom_entry = TagEntry(
            input_card.content,
            placeholder="e.g. headache, fever, nausea, fatigue...",
            height=5,
        )
        self.symptom_entry.pack(fill="x", pady=(0, 8))

        threshold_frame = tk.Frame(input_card.content, bg=COLORS["bg_card"])
        threshold_frame.pack(fill="x", pady=(0, 6))

        tk.Label(
            threshold_frame,
            text="Match Sensitivity:",
            font=FONTS["small"],
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_card"],
        ).pack(side="left")

        self.threshold_var = tk.IntVar(value=60)

        self.threshold_label = tk.Label(
            threshold_frame,
            text="60%",
            font=FONTS["small"],
            fg=COLORS["accent_teal"],
            bg=COLORS["bg_card"],
            width=4,
        )
        self.threshold_label.pack(side="right")

        slider = tk.Scale(
            input_card.content,
            from_=40,
            to=90,
            variable=self.threshold_var,
            orient="horizontal",
            bg=COLORS["bg_card"],
            fg=COLORS["text_secondary"],
            troughcolor=COLORS["bg_input"],
            activebackground=COLORS["accent_teal"],
            highlightthickness=0,
            showvalue=False,
            command=self._update_threshold_label,
        )

        slider.pack(fill="x", pady=(0, 8))

        btn_row = tk.Frame(input_card.content, bg=COLORS["bg_card"])
        btn_row.pack(fill="x", pady=(0, 6))

        EchoButton(
            btn_row,
            "🔍  Analyze Symptoms",
            command=self._run_analysis,
            style="primary",
        ).pack(side="left", fill="x", expand=True, padx=(0, 4))

        EchoButton(
            btn_row,
            "✖ Clear",
            command=self._clear_symptom_tab,
            style="ghost",
        ).pack(side="left")

        right = tk.Frame(tab, bg=COLORS["bg_dark"])
        right.grid(row=0, column=1, sticky="nsew", padx=(4, 8), pady=8)

        results_card = CardFrame(
            right,
            title="Analysis Results",
            accent=COLORS["accent_blue"],
        )
        results_card.pack(fill="both", expand=True)

        self.loading_label = tk.Label(
            results_card.content,
            text="",
            font=FONTS["body"],
            fg=COLORS["accent_teal"],
            bg=COLORS["bg_card"],
        )
        self.loading_label.pack(anchor="w", pady=(0, 4))

        self.results_bars_frame = tk.Frame(
            results_card.content,
            bg=COLORS["bg_card"],
        )
        self.results_bars_frame.pack(fill="x", pady=(0, 8))

        hsep(results_card.content)

        tk.Label(
            results_card.content,
            text="Detailed Analysis",
            font=FONTS["heading"],
            fg=COLORS["text_secondary"],
            bg=COLORS["bg_card"],
        ).pack(anchor="w", pady=(0, 4))

        self.results_text = ScrollText(results_card.content, height=14)
        self.results_text.pack(fill="both", expand=True)

    # Remaining logic methods stay unchanged (analysis, medications,
    # diet, history, navigation). Only formatting fixes were applied.
