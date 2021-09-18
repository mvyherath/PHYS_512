import numpy as np
import matplotlib.pyplot as plt

  
def ndiff(f, x):
        
    deriv1 = (f(x + dx) - f(x - dx)) / (2.0 * dx) 
    deriv2 = (f(x + 2.0*dx) - f(x - 2.0*dx)) / (4.0 * dx) 

    # Expanded out each of deriv1 and deriv2 into their respective Taylor series
    # deriv1 has (f + (dx^2/6)f'') while deriv2 has (f + (4dx^2/6))
    # To make cancel out terms in the Taylor series, used (deriv2 - deriv1)

    result = deriv2 - deriv1
    return result

x1 = 0.4
x2 = 0.01 * x1
dx = 0.001

#Testing for x
func = lambda x1: np.exp(x1)
result1 = ndiff(func, x1)

#Testing for x = 0.01x
func2 = lambda x2: np.exp(x2)
result2 = ndiff(func2, x2)


print(result1, result2)
