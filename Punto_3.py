def factorial(a)->int:
    if a == 1:
        f=1
    else:
        f= a*factorial(a-1)
    return f
    
if __name__=="__main__":
    a=int(input("Por favor ingrese un numero:"))
    print(f"El factorial de un numero es {factorial(a)}")

