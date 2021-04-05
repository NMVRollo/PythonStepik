maX = 10**6
miX = -10**6
sum = 0
for i in range(7):
    x = int(input())
    if (x <= maX or x >= miX):
        if (x % 2 == 0):
            sum += x
if sum == 0:
    print(0)
else:
    print(sum)
