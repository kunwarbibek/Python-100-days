v1=[3,4]
v2=[2,6]
# Vector addition
add = [v1[i] + v2[i] for i in range(len(v1))]
print("Addition =", add)

sub = [v1[i] - v2[i] for i in range(len(v1))]
print("vector subtraction" , sub)

mul=[v1[i]*v2[i] for i in range(len(v1))]
print("Dot product", mul)
print("***********************************************")
#****************************************

print("using numpy ")
import numpy as np
vector1= np.array([2,3])
vector2=np.array([8,9])
vector_sum=vector1+vector2
print("Addition ",vector_sum)

vector_sub=vector1-vector2
print("Subtraction",vector_sub)

dot_vector=np.dot(vector1, vector2)
print("dot vector",dot_vector)

magnitude_v1 = np.linalg.norm(v1)
print("magnitude",magnitude_v1)