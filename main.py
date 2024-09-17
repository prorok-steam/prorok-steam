#1
from math import *
r = int(input())
l = 2 * pi * r
S = pi * r ** 2
print("Длина окружности:", round(l, 2), "\n" "Площадь окружности:", round (S, 2))

#2
x, y = 10, 55
print("До замены:", x, y)
x, y = y, x
print("После замены:", x, y)

#3
from math import *
g = 9.81
L = int(input())
T = 2 * pi * ((L/g) ** 2)
print(T)