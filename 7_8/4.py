n = int(input())
print(*['*'*[i+1, n-i][i > n/2] for i in range(n)], sep='\n')