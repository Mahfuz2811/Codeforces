
n = int(input())

coordinates = []

vector0 = 0
vector1 = 0
vector2 = 0

for i in range(n):
    coordinates.append([int(j) for j in input().split()])

for i in range(n):
    vector0 += coordinates[i][0]
    vector1 += coordinates[i][1]
    vector2 += coordinates[i][2]


if vector0 == vector1 == vector2 == 0:
    print("YES")
else:
    print("NO")
