
n = int(input())
step = [5,4,3,2,1]
count = 0
step_sum = 0

while step_sum < n:
    for i in range(5):
        if step_sum + step[i] <= n:
            step_sum += step[i]
            count += 1
            break

print(count)
