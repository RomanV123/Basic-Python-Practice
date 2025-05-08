c0 = int(input("Enter a number above 1 and 0: "))
steps = 0
while (c0 != 1):
    if (c0 % 2 ==0):
        c0 = c0//2
        
    else:
        c0 = 3 * c0 + 1
    steps = steps+1
    print(c0)