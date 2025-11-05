#Declarar una matriz
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#Imprimir la matriz
print(f"Matriz A: {A}")
print(type(A))
#Acceder al dato por fila y columna
print(f"Dato: {A[2][2]}") #Fila 1, Columna 2
print(f"Dato: {A[1][0]}") #Fila 1, Columna 2
print(f"Dato: {A[0][2]}") #Fila 1, Columna 2
#Modificar un dato
A[2][2] = 10
print(f"Matriz A modificada: {A}")
#Recorrer una matriz
for filas in A:
    for elementos in filas:
        print(f"Elemento: {elementos}")

#Numpy
import numpy as np
B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(type(B)) 
B[2][2] = 10
print(f"Matriz B modificada:\n{B}")
C = np.array([
    [2, 4, 6],
    [3, 5, 7],
    [10, 1, 8]
])
print(type(C))
#Dimensiones de la matriz
print(f"Dimensiones de B: {B.shape}")
print(f"Dimensiones de C: {C.shape}")
#Operaciones entre matrices
suma = B + C
print(f"Suma de matrices:\n{suma}")
resta = B - C
print(f"Resta de matrices:\n{resta}")   
producto = B * C    
print(f"Producto de matrices:\n{producto}")
division = B / C
print(f"División de matrices:\n{division}")