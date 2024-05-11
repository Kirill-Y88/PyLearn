from sympy import *

X = Matrix([[ 5.0,  7.0, -5.0],
            [ 0.0, -2.0,  2.0],
            [-4.0, -8.0, -7.0],
            [ 1.0,  1.0,  2.0],
            [ 2.0, -1.0,  2.0],
            [ 4.0,  1.0,  4.0]])

b = Matrix([-47.0, 10.0, 63.0, -1.0, -4.0, -2.0])

# транспонируемматрицу
X.T

mul = X.T * X
print(mul)

# детерминантматрицы
mul.det()
print(mul.det())

(X.T * X)**(-1)

# формула   псевдообратной матрицы, для неквадратных матриц
X_pseudo_inverse = (X.T * X)**(-1) * X.T

best_point = X_pseudo_inverse * b

x, y, z = symbols('x, y, z')

MSE = 1 / 6 * ((5 * x + 7 * y - 5 * z + 47)**2 + \
               (- 2 * y + 2 * z - 10)**2 + \
               (-4 * x - 8 * y - 7 * z - 63)**2 + \
               (x + y + 2 * z + 1)**2 + \
               (2 * x - y + 2 * z + 4)**2 + \
               (4 * x + y + 4 * z + 2)**2)

MSE.subs({x: 0, y: 0, z: 0})

ans = MSE.subs({x: best_point[0], y: best_point[1], z: best_point[2]})

print(ans)
