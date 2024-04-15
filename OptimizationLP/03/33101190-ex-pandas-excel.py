import pandas as pd

dataMarks = pd.read_excel('data.xlsx', sheet_name='marks', engine='openpyxl')
dataPeople = pd.read_excel('data.xlsx', sheet_name='people')

dataAll = dataMarks.set_index('name').join(dataPeople.set_index('name'))

# marks = dataAll.groupby('name').mark.mean()
marks = dataAll.groupby('name').mean()

print(marks)

marks.to_excel('output.xlsx')