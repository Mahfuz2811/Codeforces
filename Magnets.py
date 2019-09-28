n = int(input())

magnets = [0]*n
count = 1

for i in range(n):
    magnets[i] = input()

for i in range(n-1):
    if magnets[i] != magnets[i+1]:
        count += 1

print(count)
