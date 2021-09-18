import numpy as np
import matplotlib.pyplot as plt

dx_vals = []
err_vals = []

  
def ndiff(fun, x):

    for dx in np.arange(0.01, 0.02, 1000):
        # Error equation derived by using dx = (eps / f''')
        t1 = fun(x + dx)
        t2 = fun(x - dx)
        t3 = 3.0 * fun(x)
        t4 = fun(x - (2.0 * dx))
        t5 = 2.0 * (fun(x - dx))
        error = t1 - t2 - t3 + t4 + t5
        #End of error equation
 
        dx_vals.append(dx)
        err_vals.append(error)
        

    calc = (fun(x + dx) - fun(x - dx)) / (2.0 * dx) 
    return calc

x = 0.1
dx = 0.01
fun = lambda x: np.exp(x)
result = ndiff(fun, x)

print(err_vals)
print(dx_vals)
print(len(dx_vals))

print(result)
print("Works")