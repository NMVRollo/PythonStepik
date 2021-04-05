from math import sqrt

n = int(input())
def MDiv(n):
    i = 2
    while n % i != 0:
       if i >= sqrt(n):
           print(n)
           return
       i += 1
    print(i)
MDiv(n)