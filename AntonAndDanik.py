n = int(input())
result = input()

aCount = dCount = 0

for ch in result:
    if ch == 'A':
        aCount += 1
    else:
        dCount += 1

if aCount > dCount:
    print('Anton')
elif dCount > aCount:
    print('Danik')
else:
    print('Friendship')
