a, b = int(input()), int(input())
sum, sum_1, num, num_1 = 0, 0, 0, 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i // j == i / j:
            sum += j
            num = i
    if sum > sum_1:
        num_1 = num
        sum_1 = sum
    if sum == sum_1:
        num_1 = max(num, num_1)
        sum_1 = sum
    num, sum = 0, 0
print(num_1, sum_1)