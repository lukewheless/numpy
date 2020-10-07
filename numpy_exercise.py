import random
import numpy as np 

grades = np.randrange(60,101,12).reshape(3,4)
 
print(grades.mean())
m = grades.mean(axis = 1)
print(m)