
word = input()

if ord(word[0]) >= 65 and ord(word[0]) <= 90:
    print(word)
else:
    cap = chr(ord(word[0])-32)
    print(word.replace(word[0], cap, 1))

