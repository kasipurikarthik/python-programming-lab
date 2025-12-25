import numpy as np
marks=[12,34,2,17,23,8,14,5,18,10]
print(marks)
arr=np.array(marks)
print("dimension of array is:",np.ndim(arr))
print("array is:",np.array(arr))
print("maximum marks of the student is:",np.max(arr))
print("minimum marks of the students is:",np.min(arr))
print("mean of the marks of students in the class is:",np.mean(arr))
print("standard deviation of marks:",np.std(arr))
print("variance of marks :",np.var(arr))
print(np.where(np.mean(arr)>10,"above average","below average"))
print("marks of the student 1 is:",arr[0])
print("marks of the student 3 is:",arr[2])
print("marks of students 2 to 6 are:", arr[1:5])
print("marks of students 3 to 8 are:", arr[2:7])

