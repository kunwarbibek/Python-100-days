import numpy as np
A = np.array([[3, 4], [7, 8]])
B = np.array([[6, 6], [7, 7]])
add = A + B
print("Matrix Addition:\n", add)

sub=A-B
print("subtraction ",sub)

mul = np.dot(A, B)
print("dot matrix", mul)
transpose_A = A.T
print("Transpose of A", transpose_A)

det_A = np.linalg.det(A)
print(" determinant", det_A)

inv_A = np.linalg.inv(A)
print("Inverse of A", inv_A)