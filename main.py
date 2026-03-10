"""
Echo Personal AI Health Assistant
Entry point — run this file to launch the application.

Usage:
    python main.py

Requirements:
    pip install fuzzywuzzy python-Levenshtein pandas Pillow
"""

import sys
import os

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def check_dependencies():
    """Check that required packages are installed."""


def main():
    check_dependencies()

    try:
        from app import EchoApp
        print("🚀 Starting Echo Health Assistant...")
        app = EchoApp()
        app.mainloop()
    except Exception as e:
        print(f"❌ Failed to start Echo: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
