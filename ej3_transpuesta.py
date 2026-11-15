"""
Ejercicio 3 - Calcular la matriz transpuesta X^T de una matriz X (lista de
listas), usando funciones lambda. La salida también es una lista de listas.

Uso:
    python3 ej3_transpuesta.py        -> ejemplo del PDF (matriz 3x4)
    python3 ej3_transpuesta.py -i     -> modo interactivo
"""
import ast
import sys

# La columna i de X se vuelve la fila i de X^T
transpuesta = lambda X: list(map(lambda i: list(map(lambda fila: fila[i], X)), range(len(X[0])))) if X else []

X = [
    [1, 2, 3, 1],
    [4, 5, 6, 0],
    [7, 8, 9, -1],
]


def imprimir(nombre, M):
    filas = len(M)
    cols = len(M[0]) if M else 0
    print(f"{nombre} ({filas}x{cols}) = [")
    for fila in M:
        print(f"  {fila},")
    print("]")


def ejecutar(M):
    if not isinstance(M, list) or not all(map(lambda f: isinstance(f, list), M)):
        print("Error: la matriz debe ser una lista de listas.")
        return
    if M and len(set(map(lambda f: len(f), M))) != 1:
        print("Error: todas las filas deben tener la misma longitud.")
        return
    imprimir("X", M)
    print()
    imprimir("Y = X^T", transpuesta(M))


def modo_interactivo():
    texto = input("Ingrese la matriz como lista de listas (Enter = ejemplo del PDF):\n> ").strip()
    try:
        M = ast.literal_eval(texto) if texto else X
    except (ValueError, SyntaxError):
        print("Error: formato inválido. Ejemplo: [[1, 2], [3, 4]]")
        return
    ejecutar(M)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-i":
        modo_interactivo()
    else:
        ejecutar(X)
