

def check_language(char):
    if char == 'H' or char == 'Q' or char == '9' or char == '+':
        return 1
    else:
        return 0


def program(p):
    i = 0
    while i < len(p): # asdf72

        if check_language(p[i]):
            return "YES"

        if p[i].isdigit():
            if int(p[i]) == 1:
                ascii_code = p[i:i+3]
                if check_language(chr(int(ascii_code))):
                    return "YES"
                i += 3
                continue
            else:
                ascii_code = p[i:i+2]
                if check_language(chr(int(ascii_code))):
                    return "YES"
                i += 2
                continue
        i += 1
    return "NO"


p = input()
print(program(p))


