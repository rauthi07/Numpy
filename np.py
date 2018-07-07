#Q1
'''import numpy as np
arr= np.random.random((10,1))
print('random no are:',arr)
print('mean are:',np.mean(arr))'''

#Q2
'''import numpy as np
arr= np.random.random((20,1))
print('random no are:',arr)
print('standrad deviation are:',np.std(arr))
print('variance are:',np.var(arr))'''


#Q3
'''import numpy as np
a=np.random.rand(10,20)
b=np.random.rand(20,25)
A=(np.dot(a,b))
print('multiplication of array:',A)
B=np.sum(A)
print('sum of array:',B)'''

#Q4
'''import numpy as np
A = np.random.rand(10,1)
print('randome integers \n',A)
def func(x):
    return (1 / (1 + np.exp(-x)))
result = np.apply_along_axis(func, 0, A)
print('new array\n',result)'''