import numpy as np

# Definimos las matrices X y Y
X = np.array([[1, 4], [0.22, 1]])
Y = np.array([[3, 5], [-2, 2]])

def calcular_determinantes(X, Y):
    # Cálculo de los determinantes (valor absoluto)
    det_X = np.abs(np.linalg.det(X))
    det_Y = np.abs(np.linalg.det(Y))
    return det_X, det_Y

def calcular_normas_matrices(X, Y):
    # Inciso 3.1: Cálculo de las normas ||X||_1, ||X||_2 y ||X||_∞
    norm_X_1 = np.linalg.norm(X, ord=1)
    norm_X_2 = np.linalg.norm(X, ord='fro')
    norm_X_inf = np.linalg.norm(X, ord=np.inf)
    
    norm_Y_1 = np.linalg.norm(Y, ord=1)
    norm_Y_2 = np.linalg.norm(Y, ord='fro')
    norm_Y_inf = np.linalg.norm(Y, ord=np.inf)
    
    # Retornamos las normas calculadas
    return norm_X_1, norm_X_2, norm_X_inf, norm_Y_1, norm_Y_2, norm_Y_inf

def calcular_inversas_y_normas(X, Y):
    # Cálculo de las inversas de X y Y
    X_inv = np.linalg.inv(X)
    Y_inv = np.linalg.inv(Y)
    
    # Cálculo de las normas ||X^-1||_1, ||X^-1||_2 y ||X^-1||_∞
    norm_X_inv_1 = np.linalg.norm(X_inv, ord=1)
    norm_X_inv_2 = np.linalg.norm(X_inv, ord='fro')
    norm_X_inv_inf = np.linalg.norm(X_inv, ord=np.inf)
    
    norm_Y_inv_1 = np.linalg.norm(Y_inv, ord=1)
    norm_Y_inv_2 = np.linalg.norm(Y_inv, ord='fro')
    norm_Y_inv_inf = np.linalg.norm(Y_inv, ord=np.inf)
    
    # Retornamos las normas inversas
    return norm_X_inv_1, norm_X_inv_2, norm_X_inv_inf, norm_Y_inv_1, norm_Y_inv_2, norm_Y_inv_inf

def calcular_condicionamiento(norm_X_1, norm_X_2, norm_X_inf, norm_Y_1, norm_Y_2, norm_Y_inf,
                              norm_X_inv_1, norm_X_inv_2, norm_X_inv_inf, norm_Y_inv_1, norm_Y_inv_2, norm_Y_inv_inf):
    # Inciso 3.2: Cálculo del número de condicionamiento para X y Y
    kappa_X_1 = norm_X_1 * norm_X_inv_1
    kappa_X_2 = norm_X_2 * norm_X_inv_2
    kappa_X_inf = norm_X_inf * norm_X_inv_inf
    
    kappa_Y_1 = norm_Y_1 * norm_Y_inv_1
    kappa_Y_2 = norm_Y_2 * norm_Y_inv_2
    kappa_Y_inf = norm_Y_inf * norm_Y_inv_inf
    
    return kappa_X_2, kappa_Y_2, kappa_X_1, kappa_Y_1, kappa_X_inf, kappa_Y_inf

def calcular_normas_y_condicionamiento(X, Y):
    # Llamamos a las funciones auxiliares para realizar los cálculos
    norm_X_1, norm_X_2, norm_X_inf, norm_Y_1, norm_Y_2, norm_Y_inf = calcular_normas_matrices(X, Y)
    norm_X_inv_1, norm_X_inv_2, norm_X_inv_inf, norm_Y_inv_1, norm_Y_inv_2, norm_Y_inv_inf = calcular_inversas_y_normas(X, Y)
    kappa_X_2, kappa_Y_2, kappa_X_1, kappa_Y_1, kappa_X_inf, kappa_Y_inf = calcular_condicionamiento(
        norm_X_1, norm_X_2, norm_X_inf, norm_Y_1, norm_Y_2, norm_Y_inf,
        norm_X_inv_1, norm_X_inv_2, norm_X_inv_inf, norm_Y_inv_1, norm_Y_inv_2, norm_Y_inv_inf
    )
    det_X, det_Y = calcular_determinantes(X, Y)

    # Resultados para cada inciso
    print("Respuesta inciso 3.1:")
    print("||X||_2:", norm_X_2)
    print("||Y||_2:", norm_Y_2)   
    print("||X^-1||_2:", norm_X_inv_2)
    print("||Y^-1||_2:", norm_Y_inv_2)

    print("\nRespuesta inciso 3.2 (Número de condicionamiento):")
    print("Número de condicionamiento kappa_2 para X:", kappa_X_2)
    print("Número de condicionamiento kappa_2 para Y:", kappa_Y_2)

    print("\nRespuesta inciso 3.3 (Determinante):")
    print("Determinante de X (pequeñez):", det_X)
    print("Determinante de Y (pequeñez):", det_Y)

    print("\nRespuesta inciso 3.4:")
    if kappa_X_2 < 10:
        print("La matriz X está bien condicionada.")
    else:
        print("La matriz X está mal condicionada.")

    if kappa_Y_2 < 10:
        print("La matriz Y está bien condicionada.")
    else:
        print("La matriz Y está mal condicionada.")

# Llamamos a la función principal para resolver el problema
calcular_normas_y_condicionamiento(X, Y)

