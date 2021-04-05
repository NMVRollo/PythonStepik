numbers = []
height = int(input())
for i in range(1, height+1):
     numbers.append(str(i))
     print(''.join(numbers + numbers[-2::-1]))