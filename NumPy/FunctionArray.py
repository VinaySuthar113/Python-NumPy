import numpy as np

#search

var = np.array([1,2,3,5,2,4,6,7])

x = np.where(var == 2)
print(x)

x = np.where((var/2) >= 1)
print(x)

x = np.where((var%2) == 1)
print(x)

#Search Sorted Array

var2 = np.array([1,2,3,4,8,9])

x1 = np.searchsorted(var2,[5,6,7],side = "left")
print(x1)


#Sort Array

var3 = np.array([3,5,6,8,24,62,4,75,334,84])

print(np.sort(var3))

var4 = np.array([[3,5],[6,8],[24,62],[4,75],[334,84]])

print(np.sort(var4))

#Filter Array

var4 = np.array(['V','I','N','A','Y'])
f = [True,False,True,False,True]
new_ar = var4[f]
print(new_ar)
print(type(new_ar))