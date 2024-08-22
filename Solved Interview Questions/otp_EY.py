order_id = input("Enter your order ID\n")
otp = 1

# Solving it without a list

for num in str(order_id):
    otp *= int(num)
print(f"Your otp is: {otp}")

# Solving this using a list

l = []
for i in str(order_id):
    l.append(int(i))

for numbers in l[:len(l)]:
    otp *= int(numbers)

print(otp)
