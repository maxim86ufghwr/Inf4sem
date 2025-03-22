import numpy as np
x = list(map(float,input().split()))
y = list(map(float,input().split()))
r=0
dx=0
dy=0
chis=0
for i in range(len(x)):
    chis += (x[i] - np.mean(x))*(y[i]- np.mean(y))
    dx = (x[i] - np.mean(x))**2
    dy = (y[i] - np.mean(y))**2
r = chis / np.sqrt(dx*dy)
dx=np.sqrt(dx/(len(x)-1))
dy=np.sqrt(dy/(len(y)-1))
print(r*(dy/dx))

# numpy
'''x1=[0,1]
y1=np.interp(x1, x, y)
print(y[1]-y[0])'''
