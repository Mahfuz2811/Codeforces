n = int(input())
soldiers = list(map(int, input().split(" ")))  # 10 10 58 31 63 40 76

minimum = 0
maximum = 0

for i in range(1, n):
    if soldiers[minimum] >= soldiers[i]:
        minimum = i
    if soldiers[maximum] < soldiers[i]:
        maximum = i


if maximum > minimum:
    result = maximum + (n - (minimum + 2))
else:
    result = maximum + (n - (minimum + 1))

print(result)
