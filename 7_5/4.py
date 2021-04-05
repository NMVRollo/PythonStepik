from numpy import prod

m = [int(i) for i in input()]
print(sum(m), len(m), prod(m), sum(m)/len(m), m[0], m[0]+m[-1], sep = '\n')