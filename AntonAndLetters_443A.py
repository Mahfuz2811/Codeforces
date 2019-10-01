set = input()

check = [0]*125
count = 0

for ch in set:
    if 'a' <= ch <= 'z' and not check[ord(ch)]:
        count += 1
        check[ord(ch)] = 1

print(count)
