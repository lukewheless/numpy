import numpy as np 

grades = np.array([[87,96,70],
                    [100,87,99],
                     [100,81,72]])

#name = ["Brad","Chad", "Bob"]

print(grades.sum())
print(grades.min())
print(grades.mean())
print(grades.var())
print(grades.std())

#for i in name:
    #print(i)

m = grades.mean(axis = 1)
print(m, end = " ")

num = np.arange(1,6)

num[1] *= 10   #mult specific num in array
print(num)

grades = np.array([[87,96,70],
                    [100,87,90]])
print(grades.reshape(1,6))  #reshapes it to one array not two
                            #ravel also does this

grades2 = np.array([[87,97,70],
                    [77,87,80]])

more_students = np.vstack(grades,grades2) #adding more students 
more_grades = np.hstack(grades,grades2) #adding more grades 














