array = [1,2,3,4,5,6,7,8,9,10]
print(array)

del array[0]
print(array)

print("length of array: ", len(array))

array.append(1000)
array.append(-5)
array.insert(5,0)
print("Appended Array: ", array)


hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

num=int(input("Enter a number:" ))
hat_list[3] = num
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
del hat_list[4]
# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)

