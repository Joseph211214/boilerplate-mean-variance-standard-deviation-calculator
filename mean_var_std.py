import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matriz = np.array(list).reshape(3, 3)

    def por_ejes(funcion):
        return [
            funcion(matriz, axis=0).tolist(),
            funcion(matriz, axis=1).tolist(),
            funcion(matriz).tolist(),
        ]

    calculations = {
        'mean': por_ejes(np.mean),
        'variance': por_ejes(np.var),
        'standard deviation': por_ejes(np.std),
        'max': por_ejes(np.max),
        'min': por_ejes(np.min),
        'sum': por_ejes(np.sum),
    }

    return calculations
