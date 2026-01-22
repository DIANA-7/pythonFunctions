# Almacenar los mesees en la variable meses y retornar tupla con el grupo de meses a partir de un numero de mes dado
def meses_faltantes(inicio,final):
    meses=("ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sept", "oct", "nov", "dic")
    return meses[inicio:final] 

#bloque principal
#se recupera desde el mes indicado hasta el otro mes indicado
print("Imprimir los nombres de meses comprendidos entre un mes y otro:")
incio=int(input("Ingrese el numero de mes: "))
final=int(input("Ingrese el numero de mes: "))
mesesfalta=meses_faltantes(incio, final)
print(mesesfalta)