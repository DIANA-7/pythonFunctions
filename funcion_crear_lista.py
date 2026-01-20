def cargar_lista():
    lista = []
    for x in range(5):
        valor=int(input("Introduce valor: "))
        lista.append(valor)
    return lista

def imprimir_mayor(lista):
    print("valores de la lista mayores a 10: ")
    for x in range(len(lista)):
        if lista[x]>10:
            print(lista[x])

lista=cargar_lista()
imprimir_mayor(lista)
