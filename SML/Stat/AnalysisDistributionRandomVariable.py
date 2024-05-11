import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.special as sps
import warnings
from scipy.stats import kurtosis
from scipy.stats import skew


plt.rcParams["figure.figsize"] = (10.0, 7.0)
warnings.filterwarnings("ignore")


ns = 10000
n_mean = 500
n_sigma = 1000

v = np.random.normal(n_mean, n_sigma, ns)
v = pd.DataFrame(v,columns = ["volume"])
v.volume = round(v.volume,0)

v.head()

# v.volume.mean()
print(v.volume.mean())
# v.volume.median()
print(v.volume.median())
print(v.volume.value_counts().nlargest(10))
print(v.volume.std())
print(np.percentile(v.volume, 50))
print(np.percentile(v.volume, 75))
# получение всей статистики  одним  методом
print(v.volume.describe())
# sns.distplot(v)
# plt.title("Распределение прибыли по пользователям группы 1")

v.volume.hist(bins = 100)
plt.title("Распределение прибыли по пользователям группы 1")
plt.show()

print(kurtosis(v.volume))
print(skew(v.volume))

def gamma_params(mean, std):
    shape = round((mean/std)**2, 4)
    scale = round((std**2)/mean, 4)
    return (shape, scale)

shape, scale = gamma_params(n_mean, n_sigma)
df = np.random.gamma(shape, scale, ns)
df = pd.DataFrame(df,columns = ["volume"])

# Округлим до целых
df.volume = round(df.volume,0)

print(df.head())


def my_basic_research(df=v, column="volume"):
    print("Базовые метрики")
    print(df[column].describe())
    print("------------------------------------")

    print("Самые популярные значения метрики, топ 5")
    print(df[column].value_counts().nlargest(5))
    print("------------------------------------")

    print("Эксцесс ", kurtosis(df[column]))
    print("Ассиметрия ", skew(df[column]))

    sns.distplot(df[column])
    plt.title("Распределение прибыли по пользователям")
    plt.show()

my_basic_research(df = df, column = "volume")
print(v[v.volume < 0].count()/len(v))
print(df[df.volume < 0].count()/len(df))
print(v[v.volume >= np.percentile(v.volume,50)].volume.sum()/10**6)
print(df[df.volume >= np.percentile(df.volume,50)].volume.sum()/10**6)






