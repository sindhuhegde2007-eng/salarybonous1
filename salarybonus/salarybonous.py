def main():
    try:
        salary = float(input("Enter the employee's salary: ₹ "))
        if salary < 0:
            print("❌ Error: Salary cannot be negative.")
        else:
            print("\n💼 Employee Salary Details")
            print(f"   Entered Salary: ₹ {salary:,.2f}")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()