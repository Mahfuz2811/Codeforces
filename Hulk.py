n = int(input()) #I hate that I love that I hate it

for i in range(1, n+1):
    if i < n:
        if i%2 == 1:
            print("I hate that", end=" ")
        else:
            print("I love that", end=" ")
    else:
        if i%2 == 1:
            print("I hate it")
        else:
            print("I love it")
