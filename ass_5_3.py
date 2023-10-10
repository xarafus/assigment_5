str1 = input("Please enter a string: ")
up = 0
low = 0
num = 0
oth = 0
for letter in str1:
    if letter.isupper():
        up += 1
    elif letter.islower():
        low += 1
    elif letter.isdigit():
        num += 1
    else:
        oth += 1
print("- Uppercase letters :", up)
print("- Lowercase letters :", low)
print("- Numbers :", num)
print("- Other characters :", oth)
