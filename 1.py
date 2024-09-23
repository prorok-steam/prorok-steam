#1
a, b = map(float, input().split())
if a == 0 or b == 0:
    print('Деление на ноль!!!')
else:
    print(round(a/b, 2))

#2
sum = float(input())
if sum > 20:
    sum = sum * 0.65
    print("Сумма:", round(sum, 2), "Скидка составила 35%")
else:
    print("Сумма:", round(sum, 2), "Скидка составила 0%")

#3
number = int(input())
if number < 1 or number > 13:
    print('yeet')
else:
    monthes = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    seasons = ['з', 'в', 'л', 'о']
    month = monthes [number - 1]
    if number in [12, 1, 2]:
        print(f'месяц: {month}\n', f'время года: {seasons[0]}')
    elif number in [3, 4, 5]:
        print(f'месяц: {month}\n', f'время года: {seasons[1]}')
    elif number in [6, 7, 8]:
        print(f'месяц: {month}\n', f'время года: {seasons[2]}')
    else:
        print(f'месяц: {month}\n', f'время года: {seasons[3]}')