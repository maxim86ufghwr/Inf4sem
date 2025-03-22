import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(16,9))
wd=[2,1,2]
hd=[2,1,2]
gs = GridSpec(ncols=3, nrows=3,figure=fig, width_ratios=wd, height_ratios=hd)

hits1=np.random.normal(0, 10, 50)
hits2=np.random.normal(0, 10, 5000)
hits3=np.random.normal(0, 100, 50000)

ax1 = plt.subplot(gs[0,0])
plt.title('50', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.hist(hits1,50)

ax2 = plt.subplot(gs[0,2])
plt.title('5000', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.hist(hits2,50)

ax3 = plt.subplot(gs[2,:])
plt.title('50000', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.hist(hits3,50)



fig.show()
