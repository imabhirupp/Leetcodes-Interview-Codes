l1 = []
l2 = []
n1 = int(input("Enter the number of elements in the first array\n"))
for i in range(0, n1):
    num1 = int(input())
    l1.append(num1)
l1.sort()

print(l1)

n2 = int(input("Enter the number of elements in the second array\n"))
for j in range(0, n2):
    num2 = int(input())
    l2.append(num2)
l2.sort(reverse=True)

print(l2)

s = 0

for num in range(0, n1):
    s = s + l1[num] * l2[num]

print(s)


