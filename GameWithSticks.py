n, m = map(int, input().split(" "))

result = n+m
if result%2 == 1:
    result -= 1

div = int(result/2)

if div%2 == 1:
    print("Akshat")
else:
    print("Malvika")
