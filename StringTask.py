
def check_vowel(ch):
    if ch.lower() == 'a' or ch.lower() == 'o' or ch.lower() == 'y' or ch.lower() == 'e' or ch.lower() == 'u' or ch.lower() == 'i':
        return True
    else:
        return False


w = input()
result = ""

for x in w:
    if check_vowel(x):
        continue
    else:
        result += "."
        result += x.lower()

print(result)



