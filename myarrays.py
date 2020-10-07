import numpy as np

integers = np.array([1,2,3])
print(integers)
print(type(integers))

integers2 = np.array([[1,2,3],[4,5,6]])

print(integers2.dtype)

print(integers2.ndim)

print(integers2.shape)

print(integers2.size)

for r in integers2:
    print(r)
    print()

for c in r:
    print(c, end=" ")
print()


for i in integers2.flat:
    print(i)

print(np.zeros(5))  #creates an array of 5 zeros

print(np.full((3,5),13))  #3 rows 5 cols of number 13

print(np.arange(5,100,5)) #goes 5 to 100 increments of 5

print(np.linespace(0.0,1.0,num = 5))

num = np.arange(1,6))
print(num*2)    #prints out array by mult each num by 2








