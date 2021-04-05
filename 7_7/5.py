a = int(input())
b = a
c = None
while b>0:
    c = b%10
    b = b//10
print(c)