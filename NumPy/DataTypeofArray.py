import numpy as np

var = np.array([1,2,3,4])
print('Data Type : ',var.dtype)

var1 = np.array([1.1,1.2,1.3])
print('Data Type : ',var1.dtype)

var2 = np.array(['a','b','c'])
print('Data Type : ',var2.dtype)

var3 = np.array([1,2,3,1.2,'a','f'])
print('Data Type : ',var3.dtype)

x = np.array([1,2,3,4,5],dtype = np.int8) # changing data type ex- int32 to int8
print('Data Type : ',x.dtype)
print(x)

x1 = np.array([1,2,3,4,5],dtype = 'f') # changing data type using shortcut keys ex- int32 to float32
print('Data Type : ',x1.dtype)
print(x1)

x2 = np.array([1,2,3,4,5]) # changing data type as a function ex- int32 to float32

new = np.float32(x2)

print('Data Type : ',x2.dtype)
print('Data Type : ',new.dtype)
print(x2)
print(new)

x3 = np.array([1,2,3,4,5])

new_1 = x3.astype(float)
print(x3)
print(new_1)