import numpy as np
import sys

n = int(input('Masukan jumlah variable : '))

#membuat array berukuran n x n-1 dan menginisiasi
#menyimpan matrix argument A/b

a = np.zeros((n,n+1))

# membuat array berukuran n dan meginisiasi
# Vektor solusi
x = np.zeros(n)

# Membaca koefisien matriks argumented
print('Masukan koefisien matriks argumented: ')
for i in range(n):
    for j in range(n+1):
        a[i][j]= float(input('a['+str(i)+']['+str(j)+']='))

# Implementasi Elimanasi Gauss Jordan
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Devide ny zero detected!')

    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][j]
            for k in range(n):
                a[j][k] = a[j][k] - ratio * a[i][k]
# Penentuan Solusi
for i in range(n):
    x[i]=a[i][n]/a[i][i]
# Menampilkan solusi
print('\n Solusi yang dibutuhkan : ')
for i in range(n):
    print('X%d = %0.6f' %(i,x[i]), end = '\t')
