n = int(input())
d = 0
for i in range(1, int(n)+1):
    for j in range(1, i+1):
        if i % j == 0:
            d += 1
    print(i, d*'+', sep ='')
    d = 0