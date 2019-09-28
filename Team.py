n = int(input())

problems = []

for i in range(n):
    problems.append([int(j) for j in input().split()])

solution = 0
count = 0

for i in range(n):
    for j in range(3):
        if problems[i][j]:
            count += 1
    if count >= 2:
        solution += 1
    count = 0

print(solution)
