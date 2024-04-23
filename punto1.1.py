import math
radio = float(input("Por favor ingrese el radio de la esfera:"))
radio_cono = float(input("Por favor ingrese el radio del cono:"))
altura = float(input("Por favor ingrese la altura del cono:"))
volumen_esfera = (lambda r1,r2,h: (((4/3)*math.pi*(r1**3))+((math.pi*(r2**2)*h)/3)))(radio,radio_cono,altura)
print(f"El volumen de una esfera con radio {radio} es {volumen_esfera}")