def calcular_cuadrado(*args) -> int:
    # Para cada numero en args se calcula el cuadrado y se imprime el resultado
    for numero in args:
        cuadrado = numero ** 2
        print(f"El cuadrado de {numero} es {cuadrado}")

# Creamos una lista de números del 1 al 100
lista = list(range(1, 101))

# Llamamos a la función para calcular los cuadrado
calcular_cuadrado(*lista)