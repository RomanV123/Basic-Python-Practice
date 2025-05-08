while True:
    print("This is a simple calculator\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    if choice == "1":
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        print("The sum is:", int1 + int2)

    elif choice == "2":
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        print("The difference is:", int1 - int2)

    elif choice == "3":
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        print("The product is:", int1 * int2)

    elif choice == "4":
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        if int2 != 0:
            print("The quotient is:", int1 / int2)
        else:
            print("Error: Division by zero is not allowed.")

    elif choice == "5":
        print("Thank you for using the calculator.")
        break

    else:
        print("Invalid input. Please enter a number from 1 to 5.")

    # Ask user if they want to continue
    continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_choice != "yes":
        print("Exiting calculator.")
        break
