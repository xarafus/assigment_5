while True:
    str1 = input("Please enter a string : ")
    if str1 == 'done':
        print("Bye!")
        break
    znaki = [',','.',':','!','?']
    str2 = ""
    for letter in str1:
        if letter not in znaki:
            str2 += letter
    up = str2.upper()
    print(up)
