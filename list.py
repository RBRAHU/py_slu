#python Merge first and last elements seperately in a list


#using Numpy array
import numpy as np
 

def merge(lst):
    arr =np.array(lst)
    return arr.T.tolist()


lst= [['x','y'],['a','b'],['1','2']]
print(merge(lst))
  