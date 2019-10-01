a = list(map(int, input().split(" "))) # 4 3 2 1

for i in range(4):
    minimum = i
    for j in range(i+1, 4):
        if a[minimum] > a[j]:
            minimum = j

    temp = a[i]
    a[i] = a[minimum]
    a[minimum] = temp

count = 0
for i in range(3):
    if a[i] == a[i+1]:
        count += 1

print(count)
