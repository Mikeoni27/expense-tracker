def add_expense(expenses: list[dict], amount: float, category: str, description: str) -> None:
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description,
    })


def delete_expense(expenses: list[dict], index: int) -> bool:
    """Delete by 1-based index. Returns True if successful."""
    if 1 <= index <= len(expenses):
        expenses.pop(index - 1)
        return True
    return False


def total_spending(expenses: list[dict]) -> float:
    return sum(e["amount"] for e in expenses)


def spending_by_category(expenses: list[dict]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals