import numpy as np
from matplotlib import pyplot as plt

xa=-1.0 * ((np.pi)/2.0)
xb= (np.pi)/2.0
x=np.linspace(xa,xb,1001)
dx=x[1]-x[0]
y=np.cos(x)

xx=np.linspace(x[6],x[-7],1001)
yy=np.empty(len(xx))
for i in range(len(xx)):
    ind=(xx[i]-x[0])/dx
    ind=int(np.floor(ind))
    x_use=x[ind-1:ind+3]
    y_use=y[ind-1:ind+3]
    p=np.polyfit(x_use,y_use,3)
    yy[i]=np.polyval(p,xx[i])
    


y_true=np.sin(xx)
if False:
    plt.ion()
    plt.clf()
    plt.plot(x,y,'*')
    plt.plot(xx,yy)

    plt.plot(xx,y_true)
    plt.show()
print('error in interpolation is ',np.std(yy-y_true))