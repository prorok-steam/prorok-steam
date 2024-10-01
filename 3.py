#1
n = int(input())
sum = 0
if n > 100:
    print('yeet!')
else:
    for i in range(1, n + 1):
        i **= 3
        sum += i
print(sum)

#2
for sh in range(1, 11):
    for dl in range(1, 11):
        print('{:2d}'.format(dl*sh), end=' ')
    print(' ')