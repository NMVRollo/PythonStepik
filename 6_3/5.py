a, b, c = len(input()), len(input()), len(input())

if a + b + c == (min(a, b, c) + max(a, b, c))/2*3:
    print("YES")
else:
    print("NO")