import numpy as np 
from pprint import pprint
p=np.array([48.349829489,2.63223494005])

# # print(p)
# print("empty:",np.empty([3,4]))
# print("dimension:",p.ndim)
# print("shape:",p.shape) 
# print(p.astype('int64'))

# print("empty_like:",np.empty_like(p))
# print("identity:",np.identity(4),np.eye(4))
# print("ones_like:",np.ones_like(p))

# print(type(np.arange(1,10)))
# print(np.full([2,3],9))
# listed=[1,2,3,4]
# b=np.asarray(listed)
# c=b.copy()
# print("C:",c)
# st="12 1 2 3 4 5 6 7 8 0"

# print(np.fromstring(st,sep=' '))
# data=[[[6,5,3,4],[1,2,7,8]],[[9,99,999,9999],[10,100,1000,10000]]]
# a=np.array(data)
# pprint(a)
# pprint(a.ndim)
# pprint(np.dot(a.T,a))
# pprint(a.swapaxes(1,2))
# pprint(a[[0,1],[2,2]])


a=np.array([[6,34,1,6],[-1,0,2,5]])
pprint(a)
# pprint(np.sort(a))
# pprint(np.sort(a,axis=0))
b=np.argsort(a)
print("b:",b)
pprint(a[0][b[0]])
pprint(np.greater(a,b))