email = input()
print('YES' if all(_ in email for _ in ('@', '.')) else 'NO')