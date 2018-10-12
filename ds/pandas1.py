import pandas as pd
import numpy as np
from pprint import pprint

labels=['a','b','c']
my_data=[10,20,30]
arr=np.array(my_data)
d={'a':10,'b':20,'c':30}

pprint(pd.Series(data=my_data,index=labels,dtype=float))
pprint(pd.Series(labels,my_data))
pprint(pd.Series(d))
e=d.copy()
e['f']=60
pprint(pd.Series(d)+pd.Series(e))