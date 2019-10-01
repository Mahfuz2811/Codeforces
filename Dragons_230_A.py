s, n = map(int, input().split(" "))
x = []
for i in range(n):
    x.append([int(j) for j in input().split(" ")])

for i in range(n):
    minimum = i
    for j in range(i+1, n):
        if x[minimum][0] > x[j][0]:
            minimum = j

    temp1 = x[i][0]
    temp2 = x[i][1]
    x[i][0] = x[minimum][0]
    x[i][1] = x[minimum][1]
    x[minimum][0] = temp1
    x[minimum][1] = temp2

flag = True
for i in range(n):
    if s > x[i][0]:
        s += x[i][1]
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
