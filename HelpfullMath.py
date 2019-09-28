
s = list(input())

for i in range(0, len(s)-1, 2):
    minimum = i
    for j in range(i+2, len(s), 2):
        if s[minimum] > s[j]:
            minimum = j

    temp = s[i]
    s[i] = s[minimum]
    s[minimum] = temp


for i in range(len(s)):
    print(s[i], end="")
