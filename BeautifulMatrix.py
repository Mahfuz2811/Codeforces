
matrix = []
flag = 0

for i in range(5):
    matrix.append([int(j) for j in input().split()])

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            flag = 1
            break
    if flag == 1:
        break

print(abs(i-2) + abs(j-2))
