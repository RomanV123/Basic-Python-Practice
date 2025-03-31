def addition(x, y):
    result = x + y
    print("Result:", result)

def multiplication(x, y):
    result = x * y
    print("Result:", result)

def division(x, y):
    if y != 0:
        result = x / y
        print("Result:", result)
    else:
        print("Cannot divide by zero!")

def exponential(x, y):
    result = x ** y
    print("Result:", result)

# Loop to keep the program running
while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Division")
    print("4. Exponential")
    print("5. Exit")
    
    num_choice = int(input("Enter a number between 1-5: "))

    if num_choice == 5:
        print("Goodbye!")
        break  # Exit the loop

    x = int(input("Enter the number x: "))
    y = int(input("Enter the number y: "))

    if num_choice == 1:
        addition(x, y)
    elif num_choice == 2:
        multiplication(x, y)
    elif num_choice == 3:
        division(x, y)
    elif num_choice == 4:
        exponential(x, y)
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")
