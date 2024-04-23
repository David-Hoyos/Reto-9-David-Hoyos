# Reto-9-David-Hoyos
## Punto 1
De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas:
### Reto6-Punto1
[![Captura-de-pantalla-2024-03-22-193634.png](https://i.postimg.cc/HxD0CRMP/Captura-de-pantalla-2024-03-22-193634.png)](https://postimg.cc/3y10XLng)

Hallar el volumen de la figura de la imagen:
```python
import math#Se importa math
radio = float(input("Por favor ingrese el radio de la esfera:"))#Se le pide al usuario el radio de la esfera
radio_cono = float(input("Por favor ingrese el radio del cono:"))#Se le pide al usuario el radio del cono
altura = float(input("Por favor ingrese la altura del cono:"))#Se le pide al usuario la altura del cono
volumen_esfera = (lambda r1,r2,h: (((4/3)*math.pi*(r1**3))+((math.pi*(r2**2)*h)/3)))(radio,radio_cono,altura)#Se define un lambda con r1,r2 y h como argumentos y se utilizan las formulas de volumen del cono y de la esfera para hallar sus volumenes para luego sumarlas y obtener el volumen total.
print(f"El volumen de una esfera con radio {radio} es {volumen_esfera}")#Se imprime el resultado
```
### Taller 1
Hallar el promedio de cinco numeros:
```python
try:#Se utiliza try para jecutar el codigo a menos que el usuario no ingrese un numero valido
    if __name__=="__main__":
        a = float(input("Por favor ingrese un numero:"))#Se le piden cinco numeros al usuario
        b = float(input("Por favor ingrese un segundo numero:"))
        c = float(input("Por favor ingrese un tercer numero:"))
        d = float(input("Por favor ingrese un cuarto numero:"))
        e = float(input("Por favor ingrese un quinto numero:"))
        promedio = (lambda a,b,c,d,e: (a+b+c+d+e)/5)(a,b,c,d,e)#Se define un lambda que tiene como argumentos cinco numeros y que los suma y los divide en 5.  
        print(f"El promedio de {a} y {b} es {promedio}")#Se imprime el resultado.
except:
    ValueError
    print("No ingresaste un numero")

```
### Reto6-Punto6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.
```python
if __name__ == "__main__":

    #Le pedimos al usuario la cantidad actual de contagiados
    contagiados = int(input("Cantidad de contagiados actuales"))

    #Le pedimos al usuario la cantidad de días para estimar el número de enfermos
    dias = int(input("Cantidad de días a estimar el número de contagiados"))

    # Calculamos el total de contagios utilizando la fórmula
    contagios = (lambda x, y: x * 2 ** y)(contagiados, dias)

    # Mostramos el número de personas contagiadas
    print(f"El número de personas contagiadas será {contagios}")
```

## Punto 2
De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
### Taller 1
Sacar el promedio de 5 numeros:
```python
ef promedio(*args)->float:#Se define una funcion con argumentos indefinidos
    suma=0#Se incializa suma y n en 0
    n = 0
    for num in args:#Se suma cada numero de args a suma y por cada uno de ellos se le suma 1 a n
        suma+=num
        n+= 1
    p= suma/n
    return p#Se devuelve la suma total de los numeros entre la cantidad de estos

if __name__=="__main__":
    a=float(input("Por favor ingrese un numero:"))#Se le piden cinco numeros al usuario
    b=float(input("Por favor ingrese un numero:"))
    c=float(input("Por favor ingrese un numero:"))
    d=float(input("Por favor ingrese un numero:"))
    e=float(input("Por favor ingrese un numero:"))
    print(f"El promedio de {a} y {b} es {promedio(a,b)}")
    print(f"El promedio de {a},{b} y {c} es {promedio(a,b,c)}")
    print(f"El promedio de {a},{b},{c} y {d} es {promedio(a,b,c,d)}")
    print(f"El promedio de {a},{b},{c},{d} y {e} es {promedio(a,b,c,d,e)}")
```
### Reto7-Punto1
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
def calcular_cuadrado(*args) -> int:
    # Para cada numero en args se calcula el cuadrado y se imprime el resultado
    for numero in args:
        cuadrado = numero ** 2
        print(f"El cuadrado de {numero} es {cuadrado}")

# Creamos una lista de números del 1 al 100
lista = list(range(1, 101))

# Llamamos a la función para calcular los cuadrados
calcular_cuadrado(*lista)
```
### Taller 1
Hallar raiz cubica de un numero.
```python
def raiz_cubica(*args)->float:#Se define la funcion
    for num in args:
        precision = 0.0001#Precision deseada
        x = num/3#Aproximacion inicial
        while True:
            x_new = (2 * x + num / (x * x)) / 3.0#Formula
            if abs(x - x_new) < precision:
                print(f"La raiz cubica de {num} es aproximadamente{x_new}")
                break
            x = x_new
if __name__=="__main__":
    a=float(input("Por favor ingrese un numero:"))#Se le piden cinco numeros al usuario
    b=float(input("Por favor ingrese un numero:"))
    c=float(input("Por favor ingrese un numero:"))
    d=float(input("Por favor ingrese un numero:"))
    e=float(input("Por favor ingrese un numero:"))
    print(f"{raiz_cubica(a,b,c,d,e)}")#Se imprime el resultado
```

## Punto 3
Escriba una función recursiva para calcular la operación de la potencia.
```python
def potencia(base : float, potencia : float) -> float:#Se define la funcion.
    if potencia == 0:#caso base
        return 1
    elif potencia == 1:
        return base
    else :
        return base * potencia(base, potencia - 1)
    
if __name__ == "__main__":
    base = float(input("Ingrese la base: "))#Se le pide al usuario la base y la potencia
    p = float(input("Ingrese la potencia: "))
    resultado = potencia(base, p)
    print(f"El resultado de {base} elevado a la {p} es: {resultado}")#Se imprime el resultado

```
## Punto 4 
Utilice la siguiente plantilla de code para contar el tiempo:
