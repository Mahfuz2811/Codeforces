
def program(s):
    for ch in s:
        if ch == 'H' or ch == 'Q' or ch == '9':
            return "YES"
    return "NO"


p = input()
print(program(p))
