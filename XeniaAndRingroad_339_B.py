n, m = map(int, input().split(" "))  # 4 3
a = list(map(int, input().split(" ")))  # 3 2 3    1 2 3    2 3 4
temp = n
count = 0

for i in range(m-1):
    if i == 0:
        count += a[i] - 1
    if a[i] == a[i+1]:
        continue
    if a[i] < a[i+1]:
        count += a[i+1] - a[i]
    else:
        count += (n+a[i+1]) - a[i]

print(count)
