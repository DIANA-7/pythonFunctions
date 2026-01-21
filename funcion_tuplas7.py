def cargar_fecha():
    dd=int(input("Ingrese numero de día: "))
    mm=int(input("Ingrese numero de mes: "))
    aa=int(input("Ingrese numero de año: "))
    tupla = (dd,mm,aa) 
    return tupla

def imprimir_fecha(fecha):
    print(fecha[0], fecha[1], fecha[2], sep="/")


#imprimir la tupla
print(cargar_fecha())

# bloque principal
#imprimir la fecha
fecha=cargar_fecha()
imprimir_fecha(fecha)