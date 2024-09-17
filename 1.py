a, b, c = map(float, input().split())
for i in range(1):
    if a % 1 != 0 or b % 1 != 0 or c % 1 != 0:
        print('Ошибка, вводите целые!')
    else:
        if b < a:
            if b < c:
                print(b)
            else:
                if a < c:
                    print(a)
                else:
                    print(c)
        else:
            print(a)

#
# a, b, c = map(int,input().split(' '))
# s = '123'
# if str(a) in s:
#     print(a)
# if str(b)in s:
#     print(b)
# if str(c) in s:
#     print(c)