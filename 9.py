import matplotlib.pyplot as plt
import numpy as np
import os

def f(x, alpha, beta):
    return (x ** beta + alpha ** beta) / x ** beta

#1
x = np.array([i for i in range(11)])

x = np.linspace(-10, 10)
plt.plot(x, f(x, 1, 1), label = '1 функция', color = 'indianred')
plt.plot(x, f(x, 2, 1), label = '2 функция', color = 'palegoldenrod')
plt.plot(x, f(x, 1, 2), label = '3 функция', color = 'darkblue')
plt.grid()
plt.title('Графики')
plt.xlabel('Абсцисс')
plt.ylabel('Ординат')
plt.legend()
plt.show()
# plt.savefig('/my_first_dependence.svg')

#2
plt.plot(x, f(x, 1, 1), label = '1', color = 'indianred')
plt.plot(x, f(x, 2, 1), label = '2 функция', color = 'palegoldenrod')
plt.plot(x, f(x, 1, 2), label = '3 функция', color = 'darkblue')
plt.grid()
plt.title('Графики')
plt.xlabel('Абсцисс')
plt.ylabel('Ординат')
plt.legend()

plt.axes([0.25, 0.50, 0.10, 0.15])
plt.title('для малых х')
plt.plot(x, f(x, 1, 1), label = '1', color = 'indianred')
plt.plot(x, f(x, 2, 1), label = '2 функция', color = 'palegoldenrod')
plt.plot(x, f(x, 1, 2), label = '3 функция', color = 'darkblue')

plt.axes([0.45, 0.60, 0.25, 0.25])
plt.title('для больших х')
plt.plot(x, f(x, 1, 1), label = '1', color = 'indianred')
plt.plot(x, f(x, 2, 1), label = '2 функция', color = 'palegoldenrod')
plt.plot(x, f(x, 1, 2), label = '3 функция', color = 'darkblue')

plt.show()
plt.savefig(dir + '9_2.png', dpi = 300)

#3
