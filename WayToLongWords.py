n = int(input())

words = []

for x in range(n):
    words.append(input())

for x in range(n):
    if len(words[x]) > 10:
        print(words[x][0] + str(len(words[x])-2) + words[x][-1])
    else:
        print(words[x])
