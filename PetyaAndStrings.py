str1 = input()
str2 = input()

flag = 0

for i in range(len(str1)):
    if str1[i].lower() != str2[i].lower():
        if ord(str1[i].lower()) > ord(str2[i].lower()):
            flag = 1
            break
        else:
            flag = -1
            break

print(flag)
