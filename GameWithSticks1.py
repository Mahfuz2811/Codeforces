n, m = map(int, input().split(" "))

if n > m:
    temp = n
    n = m
    m = temp

if n%2 == 0:
    print("Malvika")
else:
    print("Akshat")
