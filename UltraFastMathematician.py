word1 = input()
word2 = input()

for i in range(len(word1)):
    if word1[i] == word2[i]:
        print("0", end="")
    else:
        print("1", end="")
