
word = list(input())  #"hELLO", "HTTP", "z"

flag = True

for i in range(1, len(word)):
    if 'a' <= word[i] <= 'z':
        flag = False
        break

if flag:
    for i in range(len(word)):
        if 'A' <= word[i] <= 'Z':
            word[i] = chr(ord(word[i])+32)
        else:
            word[i] = chr(ord(word[i])-32)


for i in range(len(word)):
    print(word[i], end="")





