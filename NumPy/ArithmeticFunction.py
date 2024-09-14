import numpy as np

var = np.array([1,2,3,4,5,3,2])

print('min:-',np.min(var),np.argmin(var)) #min with index
print('max:-',np.max(var),np.argmax(var)) #max with index
print('sqrt:-',np.sqrt(var)) #sqrt



var1 =  np.array([[2,1,3],[9,5,6]])

print(np.min(var1,axis = 1)) #min along axis - 1 = row,0 = column


var2 = np.array([1,2,3])
print(np.sin(var2)) #sin
print(np.cos(var2)) #cos

#cumsum of [1,2,3] = 1, 1+2 ,1+2+3

var3 = np.array([1,4,5,7,4,5])

print(np.cumsum(var3))