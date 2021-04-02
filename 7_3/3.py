from math import log

n, sum = int(input()), 0

for i in range(1, n + 1):
    sum += 1 / i
print(sum - log(n))