import math


n = int(input())
coins = list(map(int, input().split(" "))) # 6 5 = 11

total_sum = 0
coin_sum = 0
count = 0

for i in range(n):
    total_sum += coins[i]

for i in range(n):
    maximum = i
    for j in range(i+1, n):
        if coins[maximum] < coins[j]:
            maximum = j
    temp = coins[i]
    coins[i] = coins[maximum]
    coins[maximum] = temp

for i in range(n):
    if coin_sum > total_sum/2:
        break
    else:
        coin_sum += coins[i]
        count += 1

print(count)


