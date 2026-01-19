print('***Suma con argumentos varibles***')

# Funcion sumar acepta argumentos variables

def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamamos a la funcion sumar
resultado = sumar(3.7,1)
print(resultado)