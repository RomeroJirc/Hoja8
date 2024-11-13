import numpy as np

# Definición de los sistemas de ecuaciones
# Sistema 1: Matriz de coeficientes y vector de términos independientes
M1 = np.array([[-0.10, 1.00],
               [0.11, -1.00]])
v1 = np.array([-2.0, 2.1])

# Sistema 2: Matriz de coeficientes y vector de términos independientes
M2 = np.array([[-0.10, 1.00],
               [0.11, -1.00]])
v2 = np.array([-2.00, 2.14])

# Número de condición de la matriz de coeficientes
numero_condicion_M1 = np.linalg.cond(M1)

# Determinante y eigenvalores de la matriz de coeficientes
determinante_M1 = np.linalg.det(M1)
autovalores_M1 = np.linalg.eigvals(M1)

# Solución exacta del primer sistema
solucion_sistema1 = np.linalg.solve(M1, v1)

# Solución exacta del segundo sistema
solucion_sistema2 = np.linalg.solve(M2, v2)

# Resultados
print("Resultado 6.1 - Solución del primer sistema (x, y):", solucion_sistema1)
print("Resultado 6.2 - Solución del segundo sistema (x, y):", solucion_sistema2)
print("Resultado 6.3 - Número de condición κ de la matriz de coeficientes:", numero_condicion_M1)
print("Resultado 6.4 - Determinante de la matriz de coeficientes:", determinante_M1)
print("Resultado 6.4 - Eigenvalores de la matriz de coeficientes:", autovalores_M1)
