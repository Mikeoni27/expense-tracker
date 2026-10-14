# Expense Tracker

A terminal app to record and analyze personal expenses. Built with
Python's standard library — no external dependencies required to run.

## Requirements

- Python 3.10+ (uses `list[dict]` and `dict[str, float]` type hints)

## Setup

    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # macOS/Linux:
    source .venv/bin/activate

## Run

    python main.py

## Usage

    1) Add   2) View   3) Delete   4) Summary   5) Quit

- **Add** — enter amount, category, description
- **View** — list all expenses with a number for each
- **Delete** — enter the number shown in View to remove an expense
- **Summary** — total spending overall and broken down by category

Expenses are saved to `data/expenses.json` automatically and reloaded
the next time you start the app.

## Running tests

    pip install pytest
    pytest -v

## Project structure

    Expense-Tracker/
    ├── main.py           # Menu and user interaction
    ├── expenses.py       # Core logic (add, delete, totals)
    ├── storage.py        # Load/save to JSON
    ├── tests/
    │   └── test_expenses.py
    └── data/             # Auto-created on first save
        └── expenses.json