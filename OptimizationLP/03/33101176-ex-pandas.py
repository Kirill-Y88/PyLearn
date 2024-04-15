import pandas as pd

df = pd.DataFrame({
    'name':['rafael','gabriel','rafael','michael'],
    'mark':[10,9,8,7]
    })

print(df.mark[2])
print(df['mark'][2])
print(df.loc[2,'mark'])
print(df.groupby('name').mean())
print(df.groupby('name').count())
print(df.mark[df.name=='rafael'])
print(df.mark[df.name=='rafael'].max())