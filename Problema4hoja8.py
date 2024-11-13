import numpy as np

# Definimos las matrices M1, M2 para los dos problemas
M1 = np.array([[0.33, 1], [1, 3]])
M2 = np.array([[4, 4], [3, 5]])

M3 = np.array([[1, 4], [0.22, 1]])
M4 = np.array([[3, 5], [-2, 2]])

def calcular_norma_infinita_y_condicionamiento(M1, M2):
    # Cálculo de la norma infinita para M1 y M2
    norm_M1_inf = np.linalg.norm(M1, ord=np.inf)
    norm_M2_inf = np.linalg.norm(M2, ord=np.inf)

    # Intentamos calcular las inversas de M1 y M2 y sus normas infinita
    try:
        M1_inv = np.linalg.inv(M1)
        norm_M1_inv_inf = np.linalg.norm(M1_inv, ord=np.inf)
    except np.linalg.LinAlgError:
        norm_M1_inv_inf = None  # No invertible

    try:
        M2_inv = np.linalg.inv(M2)
        norm_M2_inv_inf = np.linalg.norm(M2_inv, ord=np.inf)
    except np.linalg.LinAlgError:
        norm_M2_inv_inf = None  # No invertible

    # Cálculo del número de condicionamiento kappa infinito para M1 y M2
    kappa_M1_inf = norm_M1_inf * norm_M1_inv_inf if norm_M1_inv_inf is not None else None
    kappa_M2_inf = norm_M2_inf * norm_M2_inv_inf if norm_M2_inv_inf is not None else None

    # Evaluamos si están bien condicionadas según kappa infinito
    estado_M1 = "bien condicionada" if kappa_M1_inf is not None and kappa_M1_inf < 10 else "mal condicionada"
    estado_M2 = "bien condicionada" if kappa_M2_inf is not None and kappa_M2_inf < 10 else "mal condicionada"

    # Imprimimos los resultados
    print(f"Norma infinita de M1: {norm_M1_inf}")
    print(f"Norma infinita de M2: {norm_M2_inf}")
    print(f"Norma infinita de M1^-1: {norm_M1_inv_inf}")
    print(f"Norma infinita de M2^-1: {norm_M2_inv_inf}")
    print(f"Número de condicionamiento kappa_infinito para M1: {kappa_M1_inf}")
    print(f"Número de condicionamiento kappa_infinito para M2: {kappa_M2_inf}")
    print(f"La matriz M1 está {estado_M1}.")
    print(f"La matriz M2 está {estado_M2}.")

# Llamamos a la función para las matrices del inciso 2 y 3
print("Resultados para el inciso 2 usando norma infinita:")
calcular_norma_infinita_y_condicionamiento(M1, M2)

print("\nResultados para el inciso 3 usando norma infinita:")
calcular_norma_infinita_y_condicionamiento(M3, M4)
