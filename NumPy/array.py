import numpy as np
a = np.array([1,2,3]) #creating an array in numpy
print(a) 

x = [1,2,3,4]
y = np.array(x) #conversion from list to array
#print(y)
#print(type(y))
y
#dimension of array
print(y.ndim) #[](1-dimensional) , [[]](2-dimensional) , [[[]]](3-dimensiomal) , ... and so on


#creating 2-dimensional array must be in nxn form 

ar2 = np.array([[1,2,3,4],[1,2,3,4]])
print(ar2)
print(ar2.ndim)

#creating 3-dimensional array must be in nxn form 

ar3 = np.array([[[1,2,3,4],[1,2,3,4],[1,2,3,4]]])
print(ar3)
print(ar3.ndim)

#creating higher dimensional array without using multiple square brackets

arn = np.array([1,2,3,4],ndmin = 10)
print(arn)
print(arn.ndim)