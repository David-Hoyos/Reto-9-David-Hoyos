def raiz_cubica(*args)->float:
    precision = 0.00000001
    for num in args:
        precision = 0.0001
        x = num/3
        while True:
            x_new = (2 * x + num / (x * x)) / 3.0
            if abs(x - x_new) < precision:
                print(f"La raiz cubica de {num} es aproximadamente{x_new}")
                break
            x = x_new
if __name__=="__main__":
    a=float(input("Por favor ingrese un numero:"))
    b=float(input("Por favor ingrese un numero:"))
    c=float(input("Por favor ingrese un numero:"))
    d=float(input("Por favor ingrese un numero:"))
    e=float(input("Por favor ingrese un numero:"))
    print(f"{raiz_cubica(a,b,c,d,e)}")