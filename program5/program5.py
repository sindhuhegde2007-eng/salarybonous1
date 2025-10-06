# 💰 Simple Bank Deposit Program

def get_float_input(prompt):
    """Safely get a float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Amount cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("🏦 Welcome to the Deposit Calculator\n")

    # Get initial balance and deposit amount
    initial_balance = get_float_input("Enter your initial balance: ₹")
    deposit_amount = get_float_input("Enter the deposit amount: ₹")

    # Calculate updated balance
    updated_balance = initial_balance + deposit_amount

    # Display result
    print(f"\n✅ Updated Balance: ₹{updated_balance:.2f}")

if __name__ == "__main__":
    main()