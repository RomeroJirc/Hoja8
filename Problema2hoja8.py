import numpy as np

# Definimos dos nuevas matrices X y Y
X = np.array([[0.33, 1], [1, 3]])
Y = np.array([[4, 4], [3, 5]])

def calcular_normas_y_condicion(X, Y):
    # 2.1 Cálculo de las normas ||X||_2 y ||Y||_2 (norma espectral)
    norma_X_2 = np.linalg.norm(X, 2)
    norma_Y_2 = np.linalg.norm(Y, 2)
    
    # Cálculo de las inversas de X y Y, y sus normas si son invertibles
    try:
        X_inv = np.linalg.inv(X)
        norma_X_inv_2 = np.linalg.norm(X_inv, 2)
    except np.linalg.LinAlgError:
        norma_X_inv_2 = None  # No es invertible

    try:
        Y_inv = np.linalg.inv(Y)
        norma_Y_inv_2 = np.linalg.norm(Y_inv, 2)
    except np.linalg.LinAlgError:
        norma_Y_inv_2 = None  # No es invertible

    # 2.2 Cálculo del número de condicionamiento kappa para X y Y, si son invertibles
    kappa_X = norma_X_2 * norma_X_inv_2 if norma_X_inv_2 is not None else None
    kappa_Y = norma_Y_2 * norma_Y_inv_2 if norma_Y_inv_2 is not None else None
    
    # 2.3 Cálculo de la pequeñez del determinante (1 / |determinante|) si el determinante no es cero
    det_X = np.linalg.det(X)
    det_Y = np.linalg.det(Y)
    nu_X = 1 / abs(det_X) if det_X != 0 else None
    nu_Y = 1 / abs(det_Y) if det_Y != 0 else None

    # Resultados
    resultados = {
        "||X||_2": norma_X_2,
        "||Y||_2": norma_Y_2,
        "||X^-1||_2": norma_X_inv_2,
        "||Y^-1||_2": norma_Y_inv_2,
        "kappa_X": kappa_X,
        "kappa_Y": kappa_Y,
        "nu_X": nu_X,
        "nu_Y": nu_Y
    }
    return resultados

# Calculamos todos los valores
resultados = calcular_normas_y_condicion(X, Y)

# Mostramos los resultados por inciso
print("Respuesta inciso 2.1:")
print("||X||_2:", resultados["||X||_2"])
print("||Y||_2:", resultados["||Y||_2"])
print("||X^-1||_2:", resultados["||X^-1||_2"])
print("||Y^-1||_2:", resultados["||Y^-1||_2"])

print("\nRespuesta inciso 2.2:")
print("Número de condicionamiento kappa para X:", resultados["kappa_X"])
print("Número de condicionamiento kappa para Y:", resultados["kappa_Y"])

print("\nRespuesta inciso 2.3:")
print("Pequeñez del determinante de X (nu_X):", resultados["nu_X"])
print("Pequeñez del determinante de Y (nu_Y):", resultados["nu_Y"])

print("\nRespuesta inciso 2.4:")
if resultados["kappa_X"] is not None and resultados["kappa_X"] < 10:
    print("La matriz X está bien condicionada.")
else:
    print("La matriz X está mal condicionada.")

if resultados["kappa_Y"] is not None and resultados["kappa_Y"] < 10:
    print("La matriz Y está bien condicionada.")
else:
    print("La matriz Y está mal condicionada.")
