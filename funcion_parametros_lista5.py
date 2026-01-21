# PARAMETROS TIPO LISTA

def sumar(lista):
    suma=0
    for x in range(len(lista)):
        suma= suma + lista[x]
    return suma

def mayor(lista):
    may= lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may=lista[x]
    return may

def menor(lista):
    men=lista[0]
    for x in range(1, len(lista)):
        if lista[x]< men:
            men = lista[x]
    return men

listaValores = [11, 56, 35, 200, 450]
print("Lista completa: ", listaValores)
print("suma de los valores: ", sumar(listaValores))
print("el numero mayor es: ", mayor(listaValores))
print("el numero menor :", menor(listaValores))
