import numpy as np


def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n


m = int(input("Enter the order of the square matrix : "))
matrix = np.zeros([3, 3], dtype=int)


for i in range(m):
    for j in range(m):
        matrix[i][j] = int(input("Enter matrix[{}][{}] : ".format(i, j)))
a_inv = np.linalg.inv(matrix)

for i in range(8):
    x = np.dot(a_inv, x)
    lambda_1, x = normalize(x)

print('Eigenvalue:', lambda_1)
print('Eigenvector:', x)
