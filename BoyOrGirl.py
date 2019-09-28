
word = input()

positions = [0]*200

count = 0

for i in range(len(word)):
    if positions[ord(word[i])] == 0:
        count += 1
        positions[ord(word[i])] = 1

if count%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
