#1
x1, y1, z1, x2, y2, z2 = map(int, input(). split())

def find(x1, y1, z1, x2, y2, z2):
    min = 1000
    a, b, c = abs(x2 / x1), abs(y2 / y1), abs(z2 / z1)
    rad = [a, b, c]
    for i in rad:
        if i < min:
            min = i
    if min == a:
        print(x1, x2)
    elif min == b:
        print(y1, y2)
    else:
        print(z1, z2)

find(x1, x2, y1, y2, z1, z2)

#2
n = int(input())

def dvojka(n):
    osn = 2
    while osn * osn <= n and n % osn != 0:
        osn += 1
    return osn * osn > n

def palindrome(pal):
    pal = str(pal)
    return pal == pal[::-1]

for i in range (1, n + 1):
    if dvojka(i) and palindrome(i):
        print(i)