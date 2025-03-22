import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(16,9))
wd=[1,1,1]
hd=[1,1]
gs = GridSpec(ncols=3, nrows=2,figure=fig, width_ratios=wd, height_ratios=hd)
df=pd.read_csv('iris_data.csv')
le_pe=list(df['PetalLengthCm'])
wi_pe=list(df['PetalWidthCm'])
le_se=list(df['SepalLengthCm'])
wi_se=list(df['SepalWidthCm'])

a1 = plt.subplot(gs[0,0])
plt.title('x:длинна леп.;y:ширина леп.', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.plot(le_pe,wi_pe,'p',linestyle = 'None')
x1 = [0,max(le_pe)]
y1 = np.interp(x1, le_pe, wi_pe)
plt.plot(x1,y1,'r')
a1.set_xlabel('длинна леп.')
a1.set_ylabel('ширина леп.')

a2 = plt.subplot(gs[0,1])
plt.title('x:длинна леп.;y:длинна чаше.', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.plot(le_pe,le_se,'p',linestyle = 'None')
x2 = [0,max(le_pe)]
y2 = np.interp(x2, le_pe, le_se)
plt.plot(x2,y2,'r')
a2.set_xlabel('длинна леп.')
a2.set_ylabel('длинна чаше.')

a3 = plt.subplot(gs[0,2])
plt.title('x:длинна леп.;y:ширина чаше.', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.plot(le_pe,wi_se,'p',linestyle = 'None')

a4 = plt.subplot(gs[1,0])
plt.title('x:ширина леп;y:длинна чаше.', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.plot(wi_pe,le_se,'p',linestyle = 'None')
x4 = [0,max(wi_pe)]
y4 = np.interp(x4, le_pe, le_se)
plt.plot(x4,y4,'r')
a4.set_xlabel('ширина леп.')
a4.set_ylabel('длинна чаше.')

a5 = plt.subplot(gs[1,1])
plt.title('x:ширина леп.;y:ширина чаше.', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.plot(wi_pe,wi_se,'p',linestyle = 'None')

a6 = plt.subplot(gs[1,2])
plt.title('x:длинна чаше.;y:ширина чаше.', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.plot(le_se,wi_se,'p',linestyle = 'None')
plt.savefig('приложение к упражнению 4.png', dpi=300)
plt.show()

