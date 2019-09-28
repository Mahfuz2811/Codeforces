
n = int(input())

trams = []

for i in range(n):
    trams.append([int(j) for j in input().split()])

count = 0
capacity = 0

for i in range(n):
    count = count - trams[i][0]
    count = count + trams[i][1]

    if count > capacity:
        capacity = count

print(capacity)
