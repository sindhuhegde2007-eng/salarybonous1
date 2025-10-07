def main():
    try:
        salary = float(input("Enter the employee's salary: ₹ "))
        if salary < 0:
            print("❌ Error: Salary cannot be negative.")
        else:
           bonus = salary * 0.10
            total_salary = salary + bonus

            print("\n💼 Employee Salary Details")
            print(f"   Base Salary     : ₹ {salary:,.2f}")
            print(f"   Bonus (10%)     : ₹ {bonus:,.2f}")
            print(f"   Total Salary    : ₹ {total_salary:,.2f}")

    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
