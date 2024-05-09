from sympy import *

x, y, z = symbols('x, y, z')

MSE = 1 / 6 * ((5 * x + 7 * y - 5 * z + 47) ** 2 + \
               (0 * x - 2 * y + 2 * z - 10) ** 2 + \
               (-4 * x - 8 * y - 7 * z - 63) ** 2 + \
               (x + y + 2 * z + 1) ** 2 + \
               (2 * x - y + 2 * z + 4) ** 2 + \
               (4 * x + y + 4 * z + 2) ** 2)

# частные производные среднеквадратичного отклонения
MSEx = diff(MSE,x)
MSEy = diff(MSE,y)
MSEz = diff(MSE,z)
print(MSEx)
print(MSEy)
print(MSEz)
MSG = [MSEx,MSEy,MSEz]

# начальная   точка 0,0
vx = 0
vy = 0
vz = 0
# изменение положения вектора градиента
dvx = 0
dvy = 0
dvz = 0

step = 0.01
# находим значения коэффициентов a1 a2, при которых значение среднеквадратичного отклонения аппроксимирующей функции будет минимальным
for i in range(0,100):
    print('hell')
    print(i)
    vx = vx + dvx
    vy = vy + dvy
    vz = vz + dvz
    print(vx)
    print(vy)
    print(vz)
    print(MSE.subs({'x': vx, 'y': vy, 'z': vz}))
    dvx = MSG[0].subs({'x': vx, 'y': vy, 'z': vz}) * (-1*step)
    dvy = MSG[1].subs({'x': vx, 'y': vy, 'z': vz}) * (-1*step)
    dvz = MSG[2].subs({'x': vx, 'y': vy, 'z': vz}) * (-1*step)