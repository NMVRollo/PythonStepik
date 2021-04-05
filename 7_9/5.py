n = int(input())
 
s = str(n)
while len(s) > 1:
    n = 0;
    for i in s:
        n += int(i)
    s = str(n)
print(s)