
k, n, w = map(int, input().split(" "))

total_price = int(k * (w*(w+1))/2)

if n < total_price:
    print(total_price-n)
else:
    print("0")
