import scipy
from scipy.linalg import lu, lu_factor, lu_solve
import numpy as np

#Matriks A
A = np.array([[3.,-0.1,-0.2],[0.1,7.,-0.3],[0.3,-0.2,10]])

#Matriks B

b = np.array([7.85,-19.3,71.4])

#Solusi yang diberikan Lu dan b
P, L, U =lu(A)
lu, piv = lu_factor(A)
x = lu_solve((lu,piv),b)

print('Masukan P : \n ' ,P)
print('Masukan L : \n ' ,L)
print('Masukan U : \n ' ,U)
print('Masukan x : \n ' ,x)