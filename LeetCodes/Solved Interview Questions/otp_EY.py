# Solving this without any list

order_id = input("Enter your order ID\n")
otp = 1
for num in str(order_id):
    otp *= int(num)
print(f"Your otp is: {otp}")

# Creating a list with the otp numbers and then solving it

l = []

for i in str(order_id):
    l.append(int(i))

for numbers in l[:len(l)]:
    otp *= int(numbers)

print(otp)

