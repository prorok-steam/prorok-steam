#5
from array import array
from random import *
sp =  []
mat = [[random.randint(-10, 10) for i in range(10)] for i in range(10)]
for i in range(len(mat)):
    sp.append(sum(mat[i]))

#6
from random import *
m, n = map(int, input().split())
for i in range(m):
    for j in range(n):
        array = randint(1, 10)
for i in range (array):
    print(i)
print()
for j in (array):
    minimum = min(j)
    j = [(1 if minimum % 2 else 0)if g == minimum else g for g in j]
    print(*j)