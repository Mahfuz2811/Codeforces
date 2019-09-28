
n, m = map(int, input().split(" "))

puzzles = list(map(int, input().split(" "))) # 10 12 7 5 10 22 --- 5 7 10 10 12 22


for i in range(m):
    minimum = i
    for j in range(i, m-1):
        if puzzles[minimum] > puzzles[j+1]:
            minimum = j+1

    temp = puzzles[i]
    puzzles[i] = puzzles[minimum]
    puzzles[minimum] = temp


minValue =  puzzles[n-1]-puzzles[0]
for i in range(1, m-n+1): # 6 - 4 = 2
    if minValue > puzzles[i+n-1] - puzzles[i]:
        minValue = puzzles[i+n-1] - puzzles[i]


print(minValue)
