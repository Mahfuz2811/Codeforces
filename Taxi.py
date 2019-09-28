n = int(input())

groups = list(map(int, input().split(" "))) #4 3 2 2
check = [0]*n
count = 0
sum = 0

# for i in range(n):
#     maximum = i
#     for j in range(i+1, n):
#         if groups[maximum] < groups[j]:
#             maximum = j
#
#     temp = groups[i]
#     groups[i] = groups[maximum]
#     groups[maximum] = temp


for i in range(n):
    if not check[i]:
        sum += groups[i]
        check[i] = 1
        j = i+1
        count += 1
        while sum < 4:
            if i == (n-1):
                break
            if not check[j] and (sum + groups[j]) <= 4:
                sum += groups[j]
                check[j] = 1
            j += 1
            if j == n:
                break

    sum = 0

print(count)




