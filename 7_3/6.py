p = 1
for _ in range(10):
    n = int(input())
    p *= n + (n == 0)
print(p)