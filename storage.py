import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "expenses.json"


def load_expenses() -> list[dict]:
    """Load expenses from disk. Returns empty list if file doesn't exist."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_expenses(expenses: list[dict]) -> None:
    """Write expenses to disk as JSON."""
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)