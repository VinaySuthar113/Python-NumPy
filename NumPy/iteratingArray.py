import numpy as np

#Iteration 

var = np.array([1,2,3,4])
for i in var:
    print(i)
    
var1 = np.array([[1,2,3],[4,5,6]])
print()

for j in var1:
    print(j)
print()

for k in var1:
    for l in k:
        print(l)
        
print()

#using single function

for m in np.nditer(var1):
    print(m)

print()

var2 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for n in np.nditer(var2):
    print(n)
    
#with Index
var3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for a,d in np.ndenumerate(var3):
    print(a,d)