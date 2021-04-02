import math

a, b  = float(input()), float(input())
sab, pab = a + b, a * b

print(sab / 2)
print(math.sqrt(pab))
print(2 * pab / sab)
print(math.sqrt((a**2 + b**2) / 2))