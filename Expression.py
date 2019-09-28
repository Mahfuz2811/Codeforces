
a = int(input())
b = int(input())
c = int(input())
maximum = 0

maximum = (a+b+c)

if maximum < (a+b)*c:
    maximum = (a+b)*c

if maximum < a+(b*c):
    maximum = a+(b*c)

if maximum < (a*b)+c:
    maximum = (a*b)+c

if maximum < a*(b+c):
    maximum = a*(b+c)

if maximum < a*b*c:
    maximum = a*b*c

print(maximum)

