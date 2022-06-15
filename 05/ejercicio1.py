import math
def areaTriangulo(altura, base):
    return base*altura/2
def areaCirculo(radio):
    return math.pi*radio**2
print("area de un triangulo de altura 2 y base 3 es " + str(areaTriangulo(2, 3)))
print("area de un circulo de radio 5 es " + str(areaCirculo(5)))