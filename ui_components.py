"""
Echo Health Assistant - UI Components
Reusable Tkinter widgets with a clean medical theme
"""

import tkinter as tk
from tkinter import ttk

# ── Color Palette ────────────────────────────────────────────────────────────
COLORS = {
    "bg_dark": "#0D1117",
    "bg_panel": "#161B22",
    "bg_card": "#1C2333",
    "bg_input": "#21262D",
    "accent_teal": "#00D9C0",
    "accent_blue": "#58A6FF",
    "accent_purple": "#BC8CFF",
    "accent_green": "#3FB950",
    "accent_yellow": "#D29922",
    "accent_red": "#F85149",
    "text_primary": "#E6EDF3",
    "text_secondary": "#8B949E",
    "text_muted": "#484F58",
    "border": "#30363D",
    "hover": "#2D333B",
}

FONTS = {
    "title": ("Segoe UI", 22, "bold"),
    "subtitle": ("Segoe UI", 13),
    "heading": ("Segoe UI", 11, "bold"),
    "body": ("Segoe UI", 10),
    "mono": ("Consolas", 10),
    "small": ("Segoe UI", 9),
    "tag": ("Segoe UI", 8, "bold"),
}


# ── Base Card Frame ──────────────────────────────────────────────────────────
class CardFrame(tk.Frame):
    def __init__(self, parent, title=None, accent=None, **kwargs):
        kwargs.setdefault("bg", COLORS["bg_card"])
        kwargs.setdefault("relief", "flat")
        kwargs.setdefault("bd", 0)
        super().__init__(parent, **kwargs)

        bar_color = accent or COLORS["accent_teal"]
        tk.Frame(self, bg=bar_color, height=3).pack(fill="x")

        if title:
            header = tk.Frame(self, bg=COLORS["bg_card"], pady=8, padx=14)
            header.pack(fill="x")
            tk.Label(
                header,
                text=title,
                font=FONTS["heading"],
                fg=COLORS["text_primary"],
                bg=COLORS["bg_card"],
            ).pack(side="left")

        self.content = tk.Frame(self, bg=COLORS["bg_card"], padx=14, pady=6)
        self.content.pack(fill="both", expand=True)


# ── Styled Button ────────────────────────────────────────────────────────────
class EchoButton(tk.Button):
    def __init__(self, parent, text, command=None, style="primary", **kwargs):
        styles = {
            "primary": (COLORS["accent_teal"], COLORS["bg_dark"], COLORS["accent_blue"]),
            "success": (COLORS["accent_green"], COLORS["bg_dark"], "#2EA043"),
            "danger": (COLORS["accent_red"], COLORS["text_primary"], "#DA3633"),
            "ghost": (COLORS["bg_input"], COLORS["text_primary"], COLORS["hover"]),
            "purple": (COLORS["accent_purple"], COLORS["bg_dark"], "#A371F7"),
        }
        bg, fg, hover_bg = styles.get(style, styles["primary"])
        super().__init__(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg=fg,
            font=FONTS["body"],
            relief="flat",
            bd=0,
            cursor="hand2",
            activebackground=hover_bg,
            activeforeground=fg,
            padx=16,
            pady=8,
            **kwargs,
        )
        self._bg = bg
        self._hover = hover_bg
        self.bind("<Enter>", lambda e: self.config(bg=self._hover))
        self.bind("<Leave>", lambda e: self.config(bg=self._bg))


# ── Scrollable Text Display ──────────────────────────────────────────────────
class ScrollText(tk.Frame):
    def __init__(self, parent, height=12, **kwargs):
        super().__init__(parent, bg=COLORS["bg_panel"], **kwargs)
        self.text = tk.Text(
            self,
            height=height,
            bg=COLORS["bg_input"],
            fg=COLORS["text_primary"],
            font=FONTS["mono"],
            relief="flat",
            bd=0,
            wrap="word",
            padx=10,
            pady=8,
            insertbackground=COLORS["accent_teal"],
            selectbackground=COLORS["accent_blue"],
            state="disabled",
        )
        scrollbar = ttk.Scrollbar(
            self, command=self.text.yview, style="Echo.Vertical.TScrollbar"
        )
        self.text.configure(yscrollcommand=scrollbar.set)

        self.text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Text tags
        self.text.tag_configure("heading", foreground=COLORS["accent_teal"], font=FONTS["heading"])
        self.text.tag_configure(
            "body",
            foreground=COLORS["text_primary"],
            font=FONTS["body"]
        )
        self.text.tag_configure("success", foreground=COLORS["accent_green"], font=FONTS["body"])
        self.text.tag_configure("warning", foreground=COLORS["accent_yellow"], font=FONTS["body"])
        self.text.tag_configure("danger", foreground=COLORS["accent_red"], font=FONTS["body"])
        self.text.tag_configure("muted", foreground=COLORS["text_secondary"], font=FONTS["small"])
        self.text.tag_configure("purple", foreground=COLORS["accent_purple"], font=FONTS["body"])
        self.text.tag_configure("bold", foreground=COLORS["text_primary"], font=FONTS["heading"])
        self.text.tag_configure("mono", foreground=COLORS["text_primary"], font=FONTS["mono"])
        self.text.tag_configure("body", foreground=COLORS["text_primary"], font=FONTS["body"])

    def clear(self):
        self.text.config(state="normal")
        self.text.delete("1.0", "end")
        self.text.config(state="disabled")

    def append(self, text, tag=None):
        self.text.config(state="normal")
        self.text.insert("end", text, tag if tag else "")
        self.text.see("end")
        self.text.config(state="disabled")

    def set(self, text, tag=None):
        self.clear()
        self.append(text, tag)
