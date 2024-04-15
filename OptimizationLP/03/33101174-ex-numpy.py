import numpy as np

ages = np.array([10,15,20,18])
marks = np.array([9,8,5,7])

print(marks[ages%2==0])

print(np.min(ages))
print(np.max(ages))
print(np.mean(ages[marks>=7]))