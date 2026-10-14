import pytest

from expenses import (
    add_expense,
    delete_expense,
    total_spending,
    spending_by_category,
)


# ---------- add_expense ----------

def test_add_expense_appends_dict():
    expenses: list[dict] = []
    add_expense(expenses, 5000, "Food", "Lunch")
    assert expenses == [{"amount": 5000, "category": "Food", "description": "Lunch"}]


def test_add_expense_appends_to_existing_list():
    expenses = [{"amount": 100, "category": "A", "description": "x"}]
    add_expense(expenses, 200, "B", "y")
    assert len(expenses) == 2
    assert expenses[-1]["amount"] == 200


# ---------- delete_expense ----------

def test_delete_by_valid_index():
    expenses = [{"amount": 1}, {"amount": 2}, {"amount": 3}]
    assert delete_expense(expenses, 2) is True
    assert expenses == [{"amount": 1}, {"amount": 3}]


def test_delete_first_item():
    expenses = [{"amount": 1}, {"amount": 2}]
    assert delete_expense(expenses, 1) is True
    assert expenses == [{"amount": 2}]


def test_delete_out_of_range_returns_false():
    expenses = [{"amount": 1}]
    assert delete_expense(expenses, 5) is False
    assert len(expenses) == 1


def test_delete_zero_index_returns_false():
    """1-based indexing means 0 is invalid."""
    expenses = [{"amount": 1}]
    assert delete_expense(expenses, 0) is False
    assert len(expenses) == 1


# ---------- total_spending ----------

def test_total_spending_empty():
    assert total_spending([]) == 0


def test_total_spending_sums_amounts():
    expenses = [{"amount": 5000}, {"amount": 1200}, {"amount": 300}]
    assert total_spending(expenses) == 6500


def test_total_spending_handles_floats():
    expenses = [{"amount": 10.50}, {"amount": 2.25}]
    assert total_spending(expenses) == pytest.approx(12.75)


# ---------- spending_by_category ----------

def test_spending_by_category_empty():
    assert spending_by_category([]) == {}


def test_spending_by_category_groups():
    expenses = [
        {"amount": 5000, "category": "Food"},
        {"amount": 1200, "category": "Transport"},
        {"amount": 300, "category": "Food"},
    ]
    assert spending_by_category(expenses) == {"Food": 5300, "Transport": 1200}


def test_spending_by_category_single_category():
    expenses = [
        {"amount": 100, "category": "Food"},
        {"amount": 200, "category": "Food"},
    ]
    assert spending_by_category(expenses) == {"Food": 300}