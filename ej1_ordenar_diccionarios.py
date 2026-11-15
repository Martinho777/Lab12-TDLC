"""
Ejercicio 1 - Ordenar una lista de diccionarios con respecto a un key indicado,
usando funciones lambda.

Uso:
    python3 ej1_ordenar_diccionarios.py            -> ejemplo del PDF (key = 'model')
    python3 ej1_ordenar_diccionarios.py make       -> ejemplo del PDF ordenado por otra key
    python3 ej1_ordenar_diccionarios.py -i         -> modo interactivo
"""
import ast
import sys

# Ordena la lista usando una lambda que extrae el valor del key indicado
ordenar_por = lambda lista, key: sorted(lista, key=lambda d: d[key])

D = [
    {'make': 'Nokia',   'model': 216, 'color': 'Black'},
    {'make': 'Apple',   'model': 2,   'color': 'Silver'},
    {'make': 'Huawei',  'model': 50,  'color': 'Gold'},
    {'make': 'Samsung', 'model': 7,   'color': 'Blue'},
]


def imprimir(lista):
    print("[")
    for d in lista:
        print(f"  {d},")
    print("]")


def validar(lista, key):
    if not isinstance(lista, list) or not all(map(lambda d: isinstance(d, dict), lista)):
        raise ValueError("La entrada debe ser una lista de diccionarios.")
    faltantes = list(filter(lambda d: key not in d, lista))
    if faltantes:
        raise KeyError(f"El key '{key}' no existe en todos los diccionarios: {faltantes}")


def ejecutar(lista, key):
    try:
        validar(lista, key)
        print("Lista original:")
        imprimir(lista)
        print(f"\nOrdenada por key = '{key}':")
        imprimir(ordenar_por(lista, key))
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
    except TypeError:
        print(f"Error: los valores del key '{key}' no son comparables entre sí.")


def modo_interactivo():
    texto = input("Ingrese la lista de diccionarios (Enter = ejemplo del PDF):\n> ").strip()
    try:
        lista = ast.literal_eval(texto) if texto else D
    except (ValueError, SyntaxError):
        print("Error: formato inválido. Ejemplo: [{'a': 2}, {'a': 1}]")
        return
    key = input("Ingrese el key para ordenar: ").strip()
    ejecutar(lista, key)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-i":
        modo_interactivo()
    else:
        ejecutar(D, sys.argv[1] if len(sys.argv) > 1 else 'model')
