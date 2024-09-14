import numpy as np
import random

#Rand() = value between 0 and 1

var = np.random.rand(4)
print(var)

var1 = np.random.rand(2,5)
print(var1)

#Randn() - value between 0 and 1 and -ve also included

var2 = np.random.randn(5)
print(var2)

#Ranf() - value between [0.0,1.0) , 1 not included ,gives value close to 0

var3 = np.random.ranf(4)
print(var3)

#Randint(min,max,total_value) - gives random between the given range

var4 = np.random.randint(5,20,5)
print(var4)