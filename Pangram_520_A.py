n = int(input())
s = input()
check = [0]*100

for ch in s:
    check[ord(ch.upper())] = 1

flag = True
for i in range(65, 91):
    if not check[i]:
        flag = False

if flag:
    print("YES")
else:
    print("NO")
