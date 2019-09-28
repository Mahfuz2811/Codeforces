n, t = map(int, input().split(" "))
children = list(input())            #BBBGGBGGBG

while t > 0:
    i = 0
    while i < n-1:
        if children[i] == 'B' and children[i+1] == 'G':
            children[i] = 'G'
            children[i+1] = 'B'
            i += 1
        i += 1
    t -= 1

for i in range(n):
    print(children[i], end="")






