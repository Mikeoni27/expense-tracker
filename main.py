from expenses import add_expense, delete_expense, total_spending, spending_by_category
from storage import load_expenses, save_expenses


def show_expenses(expenses: list[dict]) -> None:
    if not expenses:
        print("\nNo expenses yet.\n")
        return
    print()
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. ${e['amount']:.2f}  [{e['category']}]  {e['description']}")
    print()


def prompt_add(expenses: list[dict]) -> None:
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount.\n")
        return
    category = input("Category: ").strip()
    description = input("Description: ").strip()
    add_expense(expenses, amount, category, description)
    print("Added.\n")


def prompt_delete(expenses: list[dict]) -> None:
    show_expenses(expenses)
    try:
        idx = int(input("Number to delete: "))
    except ValueError:
        print("Invalid number.\n")
        return
    print("Deleted.\n" if delete_expense(expenses, idx) else "Not found.\n")


def show_summary(expenses: list[dict]) -> None:
    print(f"\nTotal: ${total_spending(expenses):.2f}")
    for cat, amt in spending_by_category(expenses).items():
        print(f"  {cat}: ${amt:.2f}")
    print()


def main() -> None:
    expenses = load_expenses()

    while True:
        print("1) Add   2) View   3) Delete   4) Summary   5) Quit")
        choice = input("> ").strip()

        if choice == "1":
            prompt_add(expenses)
            save_expenses(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            prompt_delete(expenses)
            save_expenses(expenses)
        elif choice == "4":
            show_summary(expenses)
        elif choice == "5":
            save_expenses(expenses)
            print("Bye.")
            break
        else:
            print("Pick 1-5.\n")


if __name__ == "__main__":
    main()