import numpy as np
def funkcja_y(x):
    return 2*x**2-5*x-8

for x in np.arange(-4,5,0.5):
    print(f"f({x}) = {funkcja_y(x)}")
