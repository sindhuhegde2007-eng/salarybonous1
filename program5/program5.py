# Program to update account balance after a deposit

# Ask user for initial balance
initial_balance = float(input("Enter your initial balance: ₹"))

# Ask user for deposit amount
deposit_amount = float(input("Enter the deposit amount: ₹"))

# Calculate new balance
new_balance = initial_balance + deposit_amount

# Display the updated balance
print(f"\nYour updated balance is: ₹{new_balance:.2f}")