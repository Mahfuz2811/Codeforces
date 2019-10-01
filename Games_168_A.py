n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split(" ")])

# 1 2
# 2 4
# 3 4

count = 0
for i in range(n-1):
    for j in range(i, n-1):
        x = a[i][0]
        y = a[j+1][1]
        k = a[j+1][0]
        l = a[i][1]
        if a[i][0] == a[j+1][1]:
            count += 1
        if a[j+1][0] == a[i][1]:
            count += 1

print(count)
