n = int(input())
drinks = list(map(int, input().split(" "))) #50 50 100
sum = 0

for i in range(n):
        sum += (drinks[i]/100)

result = ((sum/n)*100)

print("%.12f" % result)

