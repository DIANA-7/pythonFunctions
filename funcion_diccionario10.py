# 1. Ingresar valores y guardarlos en nuestro diccionario
def cargar():
    diccionario={}
    continua="s"
    
    while continua=="s":
        caste = input("Ingrese palabra en castellano: ")
        ing = input("Ingrese palabra en ingles: ")
        diccionario[caste]=ing
        continua=input("Quiere cargar otra palabra:[s/n] ")
    return diccionario

'''
# Impresion del diccionario:
print(cargar())
diccionario=cargar()
'''

#2. Visualizar el contenido del diccionario en consola o las palabras en ingles y en español.
def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print(ingles, diccionario[ingles])

'''
diccionario=cargar()
imprimir(diccionario)
'''

#3. Consultar la palabla en castellano para ver su traducción al ingles.
def consulta_palabra(diccionario):
    palabra=input("Ingrese la palabra en castellano a consultar:")
    if palabra in diccionario:
        print("En ingles significa: ", diccionario[palabra])


# bloque principal
diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)

