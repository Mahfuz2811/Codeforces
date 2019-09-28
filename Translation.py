
def check_language(berland, birland):
    i = 0
    if len(berland) != len(birland):
        return "NO"

    while i < len(berland):
        if berland[i] != birland[len(berland) - i - 1]:
            return "NO"
        i += 1

    return "YES"


berland = input()
birland = input()

print(check_language(berland, birland))
