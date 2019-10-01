a = list(map(int, input().split(" ")))
b = [0]*4

for i in range(4):
    for j in range(i+1, 4):
        if a[i] == a[j]:
            b[i] += 1

count = 0
for i in range(4):
    if b[i] != 0:
        count += 1

print(count)
