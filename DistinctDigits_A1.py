l, k = map(int, input().split(" "))

while l <= k:
    num = l
    check = [0]*10
    while num:
        a = num%10
        if check[a]:
            break

        check[a] = 1
        num = int(num/10)

    if num == 0:
        break
    l += 1

if num == 0:
    print(l)
else:
    print("-1")
