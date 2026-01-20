import numpy as np
arr = np.array([10,11,12,13,14,15,16])
even_count = np.sum(arr % 2 == 0)
odd_count = np.sum(arr % 2 != 0)
print("Array:", arr)
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
