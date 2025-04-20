def math():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    total = a + b
    print("Current total:", total)

    while True:
        

        

        total += int(total)
        print("New total:", total)

def main():
    math()

if __name__ == "__main__":
    main()
