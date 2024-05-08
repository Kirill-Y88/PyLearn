from sympy import *

a2, a1, a0 = symbols('a2, a1, a0')

# среднеквадратичное отклонение
MSE = 1 / 4 * ((a1 * 1 + a2 * 2 - 5)**2 + \
               (a1 * 5 + a2 * 3 - 6)**2 + \
               (a1 * 2 + a2 * 4 - 10)**2 + \
               (a1 * 3 + a2 * 7 - 8)**2)

print(MSE)
print(diff(MSE, a2))

# частные производные среднеквадратичного отклонения
MSEa1 = diff(MSE,a1)
MSEa2 = diff(MSE,a2)

# градиент
MSG = [MSEa1,MSEa2]
print(MSEa1)
print(MSEa2)
print(MSG[0])
print(MSG[1])

# начальная   точка 0,0
va1 = 0
va2 = 0
# изменение положения вектора градиента
dva1 = 0
dva2 = 0
# находим значения коэффициентов a1 a2, при которых значение среднеквадратичного отклонения аппроксимирующей функции будет минимальным
for i in range(0,300):
    print('hell')
    print(i)
    va1 = va1 + dva1
    va2 = va2 + dva2
    print(va1)
    print(va2)
    print(MSE.subs({'a1': va1, 'a2': va2}))
    dva1 = MSG[0].subs({'a1': va1, 'a2': va2}) * (-0.01)
    dva2 = MSG[1].subs({'a1': va1, 'a2': va2}) * (-0.01)



