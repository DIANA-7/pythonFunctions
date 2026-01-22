# 1. Crear la lista de paises y su población
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



# 2. Extrae los datos de las tuplas y de la lista para visualizarlos en varias lineas
def imprimir(paises):
    print("Paises y su poblacion")
    for x in range(len(paises)):
        print(paises[x][0], paises[x][1])
     

paises = cargar_paisespoblacion() # almacena en la varialbe "paises" los datos generados por la funcion
imprimir(paises) 
print(paises)


# 3. Seleccionar e imprimir el país mas poblado

def pais_maspoblacion(paises):
    pos=0
    for x in range(1,len(paises)):
        if paises[x][1]>paises[pos][1]:
            pos=x
    print("País con mayor cantidad de habitantes: ", paises[pos][0])

pais_maspoblacion(paises)


