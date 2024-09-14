import numpy as np

#Copy and View

var = np.array([1,2,3,4])
co = var.copy()
var[1] = 40
print("var:-",var)
print("copy:-",co)

var1 = np.array([3,5,7,2,6])
var1[1] = 50
vi = var1.view()
print("var1:-",var1)
print("view:-",vi)