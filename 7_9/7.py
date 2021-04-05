a = int(input())
b = int(input())
d = 0
for i in range (a, b+1):
    d = 0
    for j in range(1, i+1):
        if i%j == 0:
            d += 1
    if d == 2:
        print(i)