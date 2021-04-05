n = int(input())
m = 1
while n>0:
    m *= n%10
    n = n//10
print(m)