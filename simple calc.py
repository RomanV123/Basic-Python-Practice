def calculator():
    count = True
    while count:
        # 1) Show menu
        print("\nSelect operation:")
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("5) Exponentiation")
        choice = input("Enter choice (1/2/3/4/5): ").strip()

        # 2) If valid choice, get numbers and compute
        if choice in ("1", "2", "3", "4", "5"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                op_name = "Sum"
            elif choice == "2":
                result = num1 - num2
                op_name = "Difference"
            elif choice == "3":
                result = num1 * num2
                op_name = "Product"
            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
                op_name = "Quotient"
            else:  # choice == "5"
                result = num1 ** num2
                op_name = f"{num1} to the power of {num2}"

            print(f"{op_name}: {result}")

        else:
            print("Invalid choice. Please select 1–5.")

        # 3) Ask to continue
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            count = False

if __name__ == "__main__":
    calculator()
