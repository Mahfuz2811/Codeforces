
def chat_room(word, s):
    j = 0
    count = 0

    for i in range(len(s)):               #aheehllleeeeeeeeoeeeooovvvlllhhellllloou
        if s[i] == word[j]:               #hello
            count += 1
            j += 1
            if count == 5:
                return "YES"

    return "NO"


s = input()
word = "hello"

print(chat_room(word, s))
