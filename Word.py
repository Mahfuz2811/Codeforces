
word = input()

lCount = 0
uCount = 0

for ch in word:
    if 'A' <= ch <= 'Z':
        uCount += 1
    else:
        lCount += 1

if uCount == lCount or lCount > uCount:
    print(word.lower())
else:
    print(word.upper())
