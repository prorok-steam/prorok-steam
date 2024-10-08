#1
stroka = "ннннннннннна"
nn = stroka.count('н')
nn_str = map(len,nn)
nn_max = max(nn_str)
print(nn, nn_max)
str = stroka.replace('н', '!')
print(str)

#2
text = "шушкрпоалт(вщопатд)"
a = text.find(r')')
print(a)

#3
str = 'абстракиця, амброзия, автомобиль'
for i in str.split():
    if str.startswith("а") or str.endswith("я"):
        print(i)