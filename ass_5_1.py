while True:
    input_str = input("Please enter two words : ")
    if input_str == 'done':
        print('-- bye!!')
        break
    elif input_str == '':
         print('-- bye!!')
         break
    words = input_str.split()
    if len(words) != 2:
        input_str = input("Please enter two words : ")
    else:
        word1, word2 = words
        if word1 < word2:
            print(f"{word1} comes first")
        elif word2 < word1:
            print(f"{word2} comes first")
