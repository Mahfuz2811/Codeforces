n = int(input())

rooms = []

for i in range(n):
    rooms.append([int(j) for j in input().split()])

count = 0

for i in range(n):
    if (rooms[i][1] - rooms[i][0]) >= 2:
        count += 1


print(count)
