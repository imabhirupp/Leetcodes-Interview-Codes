l = []
new_l = []
n = int(input("Enter the array size\n"))
num = input("Enter the numbers\n")
k = int(input("Enter the break-point\n"))
for number in num:
    l.append(number)

for i in l[k + 1:n]:
    new_l.append(i)

for j in l[0:k + 1]:
    new_l.append(j)
print(new_l)
