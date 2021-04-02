import math

n = int(input())
s = 0
r = int(math.sqrt(n))
for i in range(1, r + 1):
    if n % i == 0:
        s += i
        s += n // i
if n / r == r:
    s -= r

print(s)