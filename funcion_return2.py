# Función 1 ******************

def retorno_area(lado):
    area = lado * lado
    return area

va = int(input("Introduce el valor del lado del cuadrado: "))
superficie = retorno_area(va)

print("El area del cuadrado es: ", superficie)


# Función 2 ******************

def retorno_area(lado):
    area = lado * lado
    return area

superficie = retorno_area(5)

print("El area del cuadrado es: ", superficie)


# Función 3 ******************

def retorno_area(lado=5):
    area = lado * lado
    return area

print("El area del cuadrado es: ", superficie)