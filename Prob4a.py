import numpy as np
from matplotlib import pyplot as plt

xmin=-1.0 * ((np.pi)/2.0)
xmax= (np.pi)/2.0
npt=9
x=np.linspace(xmin,xmax,npt)
y=np.cos(x)
xx=np.linspace(x[0],x[-1],2001)


p=np.ones(len(xx))
for i in range(1,npt):
    p=p*(xx-x[i])

p=p/p[0]*y[0]

plt.ion()
plt.clf()
plt.plot(xx,p)