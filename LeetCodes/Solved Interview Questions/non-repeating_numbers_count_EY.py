num = input("Enter the string")

# Solving it with only a dictionary

char_count = {}

for char in num:
    if char in char_count:
        char_count[char] +=1
    else:
        char_count[char] = 1

print(char_count)

non_repeated_count = 0

for char in char_count:
    if char_count[char] == 1:
        non_repeated_count += 1

print(non_repeated_count)


# Solving this using a list and a dictionary

l = []
dict = {}

for i in str(num):
    l.append(i)

for char in l[:len(l)]:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print(dict)

non_repeat = 0

for char in dict:
    if dict[char] == 1:
        non_repeat += 1

print(non_repeat)
