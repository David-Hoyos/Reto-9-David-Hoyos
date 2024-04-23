def promedio(*args)->float:#Se define una funcion con argumentos indefinidos
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
    