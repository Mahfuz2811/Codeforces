
def gameStatus(n, x, y):
    check = [0]*(n+1)
    for i in range(1, x[0]+1):
        check[x[i]] = 1

    for j in range(1, y[0]+1):
        check[y[j]] = 1

    for i in range(1, n+1):
        if not check[i]:
            return "Oh, my keyboard!"

    return "I become the guy."


n = int(input())
xLevels = list(map(int, input().split(" ")))
yLevels = list(map(int, input().split(" ")))

print(gameStatus(n, xLevels, yLevels))
