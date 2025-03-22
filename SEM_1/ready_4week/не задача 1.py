import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec
import pandas as pd
fig=plt.figure(figsize=(18,8), dpi=300)

wd=[2,1,2]
hd=[2,1,4]
gs = GridSpec (ncols=3, nrows=3,figure=fig, width_ratios=wd, height_ratios=hd)
x = [i for i in range(10,100,10)]
y = [np.random.randint(1,111) for i in range(1,10)]

a1 = plt.subplot(gs[0,0])
plt.title('Common science graphic!', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.plot(x, y, 'rs--', label='just RUB, LMAO')
plt.legend()

x2 = np.arange(0, 30*np.pi, 1)
plt.xticks(x)
plt.yticks(y)
plt.grid()

a2 = plt.subplot(gs[0,2])
plt.plot(x2, 50*np.sin(x2), 'r:p', label='!SUPER SECRET!')

plt.title('Very science graphic!', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

plt.xlabel('scale of absolutely seriously things for X')
plt.ylabel('scale of absolutely seriously things for Y')

plt.grid()

plt.legend()

a3 = plt.subplot(gs[2,0])

plt.pie([0.5, 0.5, 0.01], labels = ['DUUUUUULL','Very DUUUUUUUULL','Little interesting fact'])

plt.title('Common science and Its accessories')

a4 = plt.subplot(gs[2, 2])

plt.pie([1], labels = ['INTERESTING..SUPER MEG.., oh well I think you understand me'])

plt.title('Super science and Its accessories')

#plt.savefig('mygraph.png', dpi=300)

plt.show()
