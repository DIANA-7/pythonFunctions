def cargar_paisespoblacion():
    paises=[] #lista
    for x in range(3):
        nombre=input("Ingresar el nombre del país: ")
        cantidad=int(input("Ingrese la cantidad de habitantes: "))
        
        #Creacion de una lista con 3 tuplas:
        paises.append((nombre, cantidad)) #creacion de una tupla (nombre, cantidad) antes de pasarla al metodo. Un argumento (Una tupla)
        
        #Creacion de una lista con 6 elementos:
        #paises.extend([nombre,cantidad]) #para agregar a la lista dos elementos por separado
    
    return paises

print(cargar_paisespoblacion()) # imprime la lista



# extrae los datos de las tuplas y de la lista para visualizarlos en varias lineas
def imprimir(paises):
    print("Paises y su poblacion")
    for x in range(len(paises)):
        print(paises[x][0], paises[x][1])
     

paises = cargar_paisespoblacion() # almacena en la varialbe "paises" los datos generados por la funcion
imprimir(paises) 
print(paises)


