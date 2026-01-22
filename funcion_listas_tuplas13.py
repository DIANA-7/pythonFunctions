# Almacenar los mesees en la variable meses y retornar tupla con el grupo de meses a partir de un numero de mes dado
def meses_faltantes(inicio,final):
    meses=("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sept", "oct", "nov", "dic")
    return meses[:inicio] 

#bloque principal
#se recupera todos los meses anteriores a mes indicado
print("Imprimir los nombres de meses y todos los anteriores:")
incio=int(input("Ingrese el numero de mes: "))
mesesfalta=meses_faltantes(incio)
print(mesesfalta)