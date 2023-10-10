str1 = input("Enter a string : ")
print("Input string =", str1)
letter = len(str1) - 1
while letter >= 0:
    print(str1[letter])
    letter -= 1
