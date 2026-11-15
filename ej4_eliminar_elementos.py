"""
Ejercicio 4 - Eliminar de una lista los elementos indicados en otra lista,
usando funciones lambda. La salida es la lista de elementos remanentes.

Uso:
    python3 ej4_eliminar_elementos.py       -> ejemplo del PDF
    python3 ej4_eliminar_elementos.py -i    -> modo interactivo
"""
import ast
import sys

# Conserva solo los elementos que NO están en la lista de borrado
eliminar = lambda lista, borrar: list(filter(lambda e: e not in borrar, lista))

LISTA = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
BORRAR = ['amarillo', 'café', 'blanco']


def ejecutar(lista, borrar):
    if not isinstance(lista, list) or not isinstance(borrar, list):
        print("Error: ambas entradas deben ser listas.")
        return
    print(f"Lista inicial:      {lista}")
    print(f"Elementos a borrar: {borrar}")
    no_encontrados = list(filter(lambda e: e not in lista, borrar))
    if no_encontrados:
        print(f"(No estaban en la lista: {no_encontrados})")
    print(f"Salida:             {eliminar(lista, borrar)}")


def leer_lista(mensaje, defecto):
    texto = input(mensaje).strip()
    return ast.literal_eval(texto) if texto else defecto


def modo_interactivo():
    try:
        lista = leer_lista("Ingrese la lista inicial (Enter = ejemplo del PDF):\n> ", LISTA)
        borrar = leer_lista("Ingrese la lista de elementos a borrar (Enter = ejemplo del PDF):\n> ", BORRAR)
    except (ValueError, SyntaxError):
        print("Error: formato inválido. Ejemplo: ['a', 'b', 'c']")
        return
    ejecutar(lista, borrar)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-i":
        modo_interactivo()
    else:
        ejecutar(LISTA, BORRAR)
