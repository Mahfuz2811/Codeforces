n, h = map(int, input().split(" "))

height = list(map(int, input().split(" ")))
width = 0

for i in range(n):
    if height[i] > h:
        width += 2
    else:
        width += 1

print(width)
