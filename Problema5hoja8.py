import numpy as np

# Definición de la matriz de entrada
matriz_principal = np.array([
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
])

# Cálculo del número de condición utilizando la norma de Frobenius
norma_matriz_principal = np.linalg.norm(matriz_principal, 'fro')
try:
    inversa_matriz = np.linalg.inv(matriz_principal)
    norma_inversa_matriz = np.linalg.norm(inversa_matriz, 'fro')
    numero_condicion = norma_matriz_principal * norma_inversa_matriz
except np.linalg.LinAlgError:
    numero_condicion = None  # La matriz no es invertible

# Determinante de la matriz
determinante_matriz = np.linalg.det(matriz_principal)

# Valor absoluto del determinante
magnitud_determinante_matriz = abs(determinante_matriz)

# Cálculo de los valores propios (autovalores)
autovalores = np.linalg.eigvals(matriz_principal)

# Mostrar los resultados
print("Resultado 5.1 - Número de condición (κ):", numero_condicion)
print("Resultado 5.2 - Determinante de la matriz:", determinante_matriz)
print("Resultado 5.3 - Magnitud del determinante:", magnitud_determinante_matriz)
print("Resultado 5.4 - Autovalores:", autovalores)
