import math
m, n = map(int, input().split(" "))

result = math.floor(m/2) * n

if m%2 != 0:
    result += math.floor(n/2)

print(int(result))
