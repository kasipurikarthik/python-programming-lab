import numpy as np
arr1 = [[13,14], [15,16]]
arr2 = [[4,5], [6,7]]
a = np.array(arr1)
b = np.array(arr2)
print("Array1:\n", a)
print("Array2:\n", b)
print("Dimensions of Array1:", np.ndim(a))
print("Dimensions of Array2:", np.ndim(b))
print("Sum of Arrays:\n", np.add(a, b))
print("Difference of Arrays:\n", np.subtract(a, b))
print("Multiplication of Arrays:\n", np.dot(a, b))
print("Inverse of Array1:\n",np.linalg.inv(a))
print("Transpose of Array1:\n", np.transpose(a))
print("Trace of Array1:\n", np.trace(a))
print("Trace of Array2:\n", np.trace(b))
print("Determinant of Array1:\n", np.linalg.det(a))