n = int(input())
pairs = list(map(int, input().split(" ")))

oCount = eCount = 0
pos = 0

for i in range(n):
    if pairs[i]%2 == 1:
        oCount += 1

    if pairs[i]%2 == 0:
        eCount += 1


for i in range(n):
    if oCount > eCount:
        if pairs[i]%2 == 0:
            break
    else:
        if pairs[i]%2 == 1:
            break

print(i+1)
