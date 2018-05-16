import numpy as np
import math
x1 = np.zeros(2)
x1[0] = -math.pi/2
x1[1] = math.pi/2
x1[1] += 0.000001
print("X1=",x1)

x2 = np.zeros(2)
x2[0] = -math.pi/2
x2[1] = math.pi/2
x2[1] += 0.000001
print("X2=",x2)
if x2[0] != 0:
    print("es diferente")
else:
    print("no es diferente")
