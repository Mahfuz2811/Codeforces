n = int(input())

columns = list(map(int, input().split(" ")))

for i in range(n):
    minimum = i
    for j in range(i+1, n):
        if columns[minimum] > columns[j]:
            minimum = j

    temp = columns[i]
    columns[i] = columns[minimum]
    columns[minimum] = temp

for i in range(n):
    print(columns[i], end=" ")
