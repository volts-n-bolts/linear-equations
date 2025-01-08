import numpy as np

matrix_a = np.array([
    [1, 3, 5, 4],
    [8, 16, 2, 9],
    [4, 7, 29, 7],
    [25, 16, 11, 18]
])

print(np.linalg.det(matrix_a))
print(np.linalg.inv(matrix_a))