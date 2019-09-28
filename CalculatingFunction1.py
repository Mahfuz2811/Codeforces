import math


n = int(input())

if n % 2 == 0:
    print(math.floor(n/2))
else:
    print(math.floor(n/2) - n)

