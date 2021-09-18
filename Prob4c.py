import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt


xmin=-1.0 * ((np.pi)/2.0)
xmax=(np.pi)/2.0
npt=17
x=np.linspace(xmin,xmax,npt)
y=np.cos(x)
y[-2:]=y[-3]
xx=np.linspace(x[0],x[-1],2001)



spln=interpolate.splrep(x,y)
yy=interpolate.splev(xx,spln)

plt.clf()
plt.plot(x,y,'*')
plt.plot(xx,yy)
plt.plot(xx,np.cos(xx))
plt.show()