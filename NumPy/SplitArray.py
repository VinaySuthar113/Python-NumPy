import numpy as np

var = np.array([1,2,3,4,5,6])

new_ar = np.array_split(var,3)
print(new_ar)
print(type(new_ar))

var1 = np.array([[1,2],[3,4],[5,6]])
var1 = np.array([[1,2],[3,4],[5,6]])
new_ar1 = np.array_split(var1,3)
new_ar2 = np.array_split(var1,3,axis = 1)
print(new_ar1)
print()
print(new_ar2)
print()
print(type(new_ar1))