def palindrome():
    num = input("Enter a number\n")
    l = []
    b = str()                        # declaring b as a string integer
    for digits in str(num):
        l.append(digits)
    for i in l[::-1]:                # accessing the list in the reverse order
        b = b + i                    # concatinating with i with b in order to get the reverse of the number
    if num == b:
        print(f"Palindrome {num}")
    else:
        return ("Not a palindrome")

palindrome()