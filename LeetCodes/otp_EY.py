order_id = input("Enter your order ID\n")
otp = 1
for num in str(order_id):
    otp *= int(num)
print(f"Your otp is: {otp}")

# Creating a list with the otp numbers
# for i in str(order_id):
#     l.append(int(i))

