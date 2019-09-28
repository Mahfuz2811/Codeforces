
n = int(input())

friends = list(map(int, input().split(" ")))

numbers = [0]*n

for i in range(1, n+1):
    for j in range(n):
        if i == friends[j]:
            numbers[i-1] = j+1
            break

for i in range(n):
    print(numbers[i], end=" ")
