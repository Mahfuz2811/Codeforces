
def check_lucky(lucky_number):
    lucky_number = str(lucky_number)
    lucky_count = 0
    for i in lucky_number:
        if i == '4' or i == '7':
            lucky_count += 1

    if lucky_count == len(lucky_number):
        return 1
    else:
        return 0



number = input()
count = 0

for digit in number:
    if digit == '4' or digit == '7':
        count += 1


if check_lucky(count):
    print("YES")
else:
    print("NO")
