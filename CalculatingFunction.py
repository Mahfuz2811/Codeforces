import math


fn = int(input())

n = math.floor(fn/2)
evenSum = n*(n+1)

n = math.ceil(fn/2)
oddSum = int((n/2)*(2+(n-1)*2))

print(evenSum - oddSum)

