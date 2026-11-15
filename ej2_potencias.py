"""
Ejercicio 2 - Calcular la potencia n-ésima de cada elemento de una lista de
enteros, usando funciones lambda. n debe ser un entero positivo (n ∈ Z+).

Uso:
    python3 ej2_potencias.py          -> ejemplo del PDF (lista 1..10, n = 3)
    python3 ej2_potencias.py 2        -> lista 1..10 con otra n
    python3 ej2_potencias.py -i       -> modo interactivo
"""
import ast
import sys

# Aplica la lambda x -> x^n a cada elemento de la lista
potencias = lambda lista, n: list(map(lambda x: x ** n, lista))

LISTA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def ejecutar(lista, n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        print(f"Error: n = {n} no es un entero positivo (n ∈ Z+).")
        return
    if not isinstance(lista, list) or not all(map(lambda x: isinstance(x, int) and not isinstance(x, bool), lista)):
        print("Error: la entrada debe ser una lista de enteros.")
        return
    print(f"Lista inicial: {lista}")
    print(f"n = {n}")
    print(f"Salida:        {potencias(lista, n)}")


def leer_n(texto):
    try:
        return int(texto)
    except ValueError:
        return texto


def modo_interactivo():
    texto = input("Ingrese la lista de enteros (Enter = [1..10]):\n> ").strip()
    try:
        lista = ast.literal_eval(texto) if texto else LISTA
    except (ValueError, SyntaxError):
        print("Error: formato inválido. Ejemplo: [1, 2, 3]")
        return
    ejecutar(lista, leer_n(input("Ingrese n: ").strip()))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-i":
        modo_interactivo()
    else:
        ejecutar(LISTA, leer_n(sys.argv[1]) if len(sys.argv) > 1 else 3)
