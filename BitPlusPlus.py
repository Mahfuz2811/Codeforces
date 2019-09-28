n = int(input())

bits = list()

for i in range(n):
    bits.append(input())

result = 0;

for i in range(n):
    if '++' in bits[i]:
        result += 1
    else:
        result -= 1

print(result)
