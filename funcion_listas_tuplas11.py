# Almacenar los mesees en la variable meses y retornar tupla con el grupo de meses a partir de un numero de mes dado
def meses_faltantes(numero):
    meses=("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sept", "oct", "nov", "dic")
    return meses[numero:]

#bloque principal
#se recupera desde el mes indicado hasta el final de la lista
print("Imprimir los nombres de meses que faltan hasta fin de año")
numero=int(input("Ingrese el numero de mes: "))
mesesfalta=meses_faltantes(numero)
print(mesesfalta)

