try:
    if __name__=="__main__":
        a = float(input("Por favor ingrese un numero:"))
        b = float(input("Por favor ingrese un segundo numero:"))
        promedio = (lambda a,b: (a+b)/2)(a,b)
        print(f"El promedio de {a} y {b} es {promedio}")
except:
    ValueError
    print("No ingresaste un numero")
