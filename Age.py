name = input("What is your name? ")
age = input("How old are you? ")

try:
    print("Your name is " + name + " and you will be 100 in " + str(100 - int(age)) + " years.")
except ValueError:
    print("Please enter a valid number for your age.")

    