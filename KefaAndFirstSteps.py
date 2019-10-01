n = int(input())
steps = list(map(int, input().split(" "))) #2 2 3 4
count = 1
fCount = 0

for i in range(n-1):
    if steps[i] <= steps[i+1]:
        count += 1
    else:
        if fCount < count:
            fCount = count
        count = 1


if count > fCount:
    print(count)
else:
    print(fCount)
