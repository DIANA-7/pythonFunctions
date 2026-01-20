# Funcion con parametros arbitrarios
def sumar(v1, v2, *lista): 
    suma = v1 + v2
    for i in range(len(lista)):
        suma += lista[i]    
    return suma

print("suma de dos valores")
print(sumar(1,2))
print("suma de cuatro valores")
print(sumar(1,2,3,4))
print("suma de diez valores")
print(sumar(1,2,3,4,5,6,7,8,9,10))           
