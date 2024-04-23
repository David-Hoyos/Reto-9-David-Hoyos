try:
    if __name__=="__main__":
        a = int(input("Por favor ingrese un numero:"))
        b = a-1
        factorial = lambda a: 1 if a == 0 else a* factorial(a-1)
        print(f"El factorial de {a} es {factorial(a)}")
except:
    ValueError
    print("No ingresaste un numero valido")