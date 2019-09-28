import math

n = int(input())
groups = list(map(int, input().split(" "))) #4 3 2 2
count = 0
g1 = g2 = g3 = g4 = 0

for i in range(n):
    if groups[i] == 1:
        g1 += 1
    elif groups[i] == 2:
        g2 += 1
    elif groups[i] == 3:
        g3 += 1
    else:
        g4 += 1

count += g4
g4 = 0

count += math.floor(g2/2)
g2 = g2%2

if g3 >= g1:
    count += g3
    count += g2
else:
    count += g3
    g1 = g1 - g3
    count += math.ceil((g1 + (g2*2))/4)

print(count)
