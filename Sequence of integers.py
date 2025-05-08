number = input("Enter a sequence of integers: ").split()
integers = [int(i) for i in number]

total = sum(integers)
print("The sum of the integers is:", total)

count = len(integers)
print("The number of integers is:", count)

average = total / count
print("The average of the integers is:", average)

largest = max(integers)
print("The largest integer is:", largest)

smallest = min(integers)
print("The smallest integer is:", smallest)