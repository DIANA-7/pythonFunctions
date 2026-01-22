''' 
Problema: 
Confeccionar un programa que permita cargar un codigo 
de producto como clave en un diccionario. Guardar para
dich clave el nombre del producto. Su precio y cantidad en
stock.
Implementar las siguientes actividades:
1. Carga de datos en el diccionario
2. Listado completo de productos
3. Consulta de un producto por su clave, mostrar el nombre,
precio y stock.
4. Listado de todos los productos que tengan un stock con 
valor cero.

'''

# 1. Cargar los productos en el diccionario "productos":

def cargar():
    productos={}   # diccionario
    continua="s"
    while continua == "s":
        codigo=int(input("Ingrese el codigo del producto: "))
        descripcion=(input("Ingrese la descripcion: "))
        precio=float(input("Ingrese el precio: "))
        stock=int(input("Ingrese el stock actual: "))
        productos[codigo]=(descripcion, precio, stock) # estructura para almacenar elementos en el diccionario
        continua=input("Desea cargar otro producto[s/n]?")
    return productos


# 2. Imprime el listado completo de productos:

def imprimir(productos):
    print("listado completo de productos: ")
    for codigo in productos:
        print(codigo, productos[codigo][0], productos[codigo][1],productos[codigo][2])


# 3. Consulta por codigo de producto y los datos relacionados:

def consulta(productos):
    codigo=int(input("Ingrese el codigo de articulo a consultar: "))
    if codigo in productos:
        print(productos[codigo][0], productos[codigo][1], productos[codigo][2])


# 4. Consultar la lista de articulos con stock cero:

def listado_stock_cero(productos):
    print("Listado de articulos con stock en cero:")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])


productos=cargar()
imprimir(productos)
consulta(productos)
listado_stock_cero(productos)
    

