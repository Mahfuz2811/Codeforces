
a, b = map(int, input().split(" ")) # 4, 7

year = 0

while a <= b:
    a = a * 3
    b = b * 2
    year += 1

print(year)
