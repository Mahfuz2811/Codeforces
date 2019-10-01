l, r = map(int, input().split(" ")) #121 130
notDistinct = False

while l <= r:
    check = [0]*100
    flag = True
    for ch in str(l):
        if check[ord(ch)]:
            flag = False
        check[ord(ch)] = 1

    if flag:
        print(l)
        notDistinct = True
        break

    l = int(l) + 1

if not notDistinct:
    print("-1")
