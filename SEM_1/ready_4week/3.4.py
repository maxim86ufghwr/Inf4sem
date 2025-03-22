import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(16,9))
wd=[1]
hd=[1,1]
gs = GridSpec(ncols=1, nrows=2,figure=fig, width_ratios=wd, height_ratios=hd)

a1 = plt.subplot(gs[0,0])
df=pd.read_csv('iris_data.csv')
sort=list(df['Species'])
sort_int=[]
sort_l=[]
rrrr=set()
for i in sort:
    rrrr.add(i)
for i in rrrr:
    s=sort.count(i)
    sort_int.append(s / len(sort))
    sort_l.append(i)
plt.pie(sort_int, labels = sort_l)

a1 = plt.subplot(gs[1,0])
df=pd.read_csv('iris_data.csv')
ll=[0,0,0]
length=list(map(float, df['PetalLengthCm']))
for i in length:
    if i <= 1.2:
        ll[0]+=1
    if i >= 1.5:
        ll[2]+=1
    if i <= 1.5 and i >= 1.2:
        ll[1] += 1
for i in ll:
    print(i)
ll[0]/=len(length)
ll[1]/=len(length)
ll[2]/=len(length)
plt.pie(ll, labels = ['less 1.2','between 1.2 , 1.5','more than 1.5'])
fig.show()
