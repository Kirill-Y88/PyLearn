import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # для отрисовки 3D проекции

# matplotlib.rc("font", size=18) # для увеличения шрифта подписей графиков

# загружаем данные
houses = pd.read_csv("1.4_houses.csv")
houses2 = pd.read_csv("1.4_housestest.csv")
houses.head(7)

# импортируем модуль, отвечающий за деревья решений
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

# выгружаем признаки и целевые значения в отдельные переменные
X = houses[["dim_1", "dim_2"]]
y = houses["level"]
X2 = houses2[["dim_1", "dim_2"]]

# создаем классификатор
cl = DecisionTreeClassifier().fit(X, y)


# выведем информацию для интерпретации построенной модели
print(export_text(cl))

# проведем классификацию
cl.predict(X[7:8])[0], y[7]

print(X[2:3])
print(cl.predict(X[2:3])[0], y[3])
print(X2[3:4])
print(cl.predict(X2[3:4])[0])

