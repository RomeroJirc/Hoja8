import numpy as np

# Creación de la matriz B
B = np.array([[1, 0, -4, 1],
              [4, 5, 7, 0],
              [1, -2, 0, 3]])

# Cálculo de la norma 1 (suma de valores absolutos por columnas)
norma_col = np.max(np.sum(np.abs(B), axis=0))

# Cálculo de la norma de Frobenius
norma_frobenius = np.sqrt(np.sum(np.power(B, 2)))

# Cálculo de la norma infinita (suma de valores absolutos por filas)
norma_fila_max = np.max(np.sum(np.abs(B), axis=1))

# Muestra de resultados
print(f"Norma 1 (por columna): {norma_col}")
print(f"Norma de Frobenius: {norma_frobenius}")
print(f"Norma infinita (por fila): {norma_fila_max}")
