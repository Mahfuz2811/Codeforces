
import math


def check_lucky_number(number):
    number = str(number)
    count = 0

    for i in number:
        if i == '4' or i == '7':
            count += 1

    if count == len(number):
        return 1
    else:
        return 0


def almost_lucky(number):
    for i in range(1, math.floor(number/2) + 1):
        if number % i == 0 and check_lucky_number(i):   # if the number is dividable some lucky number
            return 1
    return 0


lucky_number = int(input())

if check_lucky_number(lucky_number):
    print("YES")
else:
    if almost_lucky(lucky_number):
        print("YES")
    else:
        print("NO")

