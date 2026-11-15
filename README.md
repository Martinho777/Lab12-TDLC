# Laboratorio No. 12 – Funciones lambda en Python

Teoría de la Computación — Universidad del Valle de Guatemala

## Video

▶️ [Ver video de ejecución](https://uvggt-my.sharepoint.com/:f:/r/personal/vil24033_uvg_edu_gt/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fvil24033%5Fuvg%5Fedu%5Fgt%2FDocuments%2F6o%2E%20Semestre%2FTDLC%2FVideo%20Lab%2012&share=cgr%2D7lE2sZq0QZ9HV0tb6w1XEgUCZvzneOCoSezvTXdR8P7khg)

## Requisitos

- Python 3.8 o superior (no se necesitan librerías externas)

## Ejercicios

| Archivo | Descripción |
|---|---|
| `ej1_ordenar_diccionarios.py` | Ordena una lista de diccionarios según un key indicado (`sorted` + `lambda`) |
| `ej2_potencias.py` | Calcula la potencia n-ésima de cada elemento de una lista (`map` + `lambda`) |
| `ej3_transpuesta.py` | Calcula la transpuesta de una matriz dada como lista de listas (`map` + `lambda`) |
| `ej4_eliminar_elementos.py` | Elimina de una lista los elementos indicados en otra lista (`filter` + `lambda`) |

## Ejecución

Cada programa tiene tres formas de ejecutarse:

1. **Sin argumentos**: corre el ejemplo del enunciado.
2. **Con argumento** (ejercicios 1 y 2): cambia el parámetro del ejemplo.
3. **Con `-i`**: modo interactivo para ingresar datos propios (si se presiona Enter se usa el ejemplo).

### Ejercicio 1 – Ordenar diccionarios

```bash
python3 ej1_ordenar_diccionarios.py          # ordena por 'model'
python3 ej1_ordenar_diccionarios.py make     # ordena por 'make'
python3 ej1_ordenar_diccionarios.py -i       # interactivo
```

### Ejercicio 2 – Potencias

```bash
python3 ej2_potencias.py         # lista [1..10], n = 3
python3 ej2_potencias.py 2       # lista [1..10], n = 2
python3 ej2_potencias.py -i      # interactivo
```

### Ejercicio 3 – Matriz transpuesta

```bash
python3 ej3_transpuesta.py       # matriz 3x4 del enunciado
python3 ej3_transpuesta.py -i    # interactivo
```

### Ejercicio 4 – Eliminar elementos

```bash
python3 ej4_eliminar_elementos.py       # ejemplo del enunciado
python3 ej4_eliminar_elementos.py -i    # interactivo
```

## Casos que manejan los programas

- **Ej. 1**: ordenar por cualquier key (numérica o de texto); error si el key no existe en todos los diccionarios o si los valores no son comparables.
- **Ej. 2**: cualquier n ∈ Z+; error si n es 0, negativo o no es entero, o si la lista no es de enteros.
- **Ej. 3**: matrices cuadradas y rectangulares, matriz vacía; error si las filas tienen longitudes distintas.
- **Ej. 4**: elementos a borrar que no están en la lista se ignoran (y se reportan); listas vacías.
