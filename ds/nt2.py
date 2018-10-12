from pprint import pprint
import numpy as np 

a=np.array([[1,2],[3,4]])
pprint(a)
# pprint(np.sum(a, axis=1))
# pprint(np.prod(a, axis=1))
# pprint(np.diff(a, axis=1))
pprint(np.std(a))