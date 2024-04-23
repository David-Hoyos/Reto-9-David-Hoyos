import time #Se importa time.

def fibonacci(n : int )-> int: #Se define la funcion.
  if n <=1:
    # caso base
    return 1 
  else:
    # condición
    return fibonacci(n-1)+fibonacci(n-2)  
#Se inician timer y number en 0
timer=0 
number = 0
while timer<=10: #Se establece que el "tiempo significativo" es más de 10 segundos, así que se hace el cáculo para los números que tome menos de 10 segundos.
    start_time = time.time() #Tiempo de inicio
    serie_fibonacci = fibonacci(number) #Se evalúa la función fibonacci con number.
    print(f"El numero de la serie de Fibonacci en la posicion {number} es {serie_fibonacci}")
    end_time = time.time() #Tiempo final.
    timer = end_time - start_time #Tiempo que tomó hallar el número en la posición.
    print(timer) #Se imprime el tiempo.
    number+=1 #Se suma 1 a number para continuar con el siguiente número.
print("Si tomamos como tiempo significativo 10 segundos, el tiempo empieza a ser significativo en el término",number-1,"de la serie.")
#Desde 
