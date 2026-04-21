import random
import string

x = int(input("Enter the length of the password: "))
password = ''.join(random.choices(string.ascii_letters + string.digits, k=x))
print("Generated password:", password)