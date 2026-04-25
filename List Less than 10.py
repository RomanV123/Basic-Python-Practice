
a = [1,2,3,4,5,6,7,8,9,10]
print(a[0:5])
print(a[5:10])

for i in range(0, 5):
    print(a[i])


b = []
num = int(input("Enter a number: "))
b.append(num)
print(b)

for i in range(len(a)):
    if a[i]<num:
        b.append(a[i])
        
print(b)




