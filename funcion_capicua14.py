''' 
El algoritmo clásico para determinar si una palabra o número es palíndromo (o "capicúa" cuando hablamos de números). 
Básicamente, verifica si se lee igual de izquierda a derecha que de derecha a izquierda.
''' 

def proceso(cadena):
    ultimos=-1
    iguales=0

    # Bucle que solo recorre la mitad de la cadena. 
    # Se usa // (división entera) porque si la cadena tiene 4 letras, 
    # solo necesitamos comparar 2 parejas. No hace falta llegar al final.
    for primeros in range(0,len(cadena)//2):
        if cadena[primeros]==cadena[ultimos]: # Compara el carácter de la posición actual x (que va de izquierda a derecha: 0, 1, 2...) 
                                                # con el carácter en la posición indice (que va de derecha a izquierda: -1, -2, -3...).
            iguales=iguales+1 #Si los caracteres coinciden, suma 1 al contador de "parejas iguales".
        ultimos=ultimos-1  #Mueve el puntero del final un paso hacia la izquierda para que en la siguiente vuelta compare el penúltimo, 
                            # luego el antepenúltimo, y así sucesivamente.
    print(cadena)
    
    # si el número de parejas iguales es exactamente igual a la mitad de la longitud de la cadena, 
    # significa que todas las comparaciones fueron exitosas.
    if iguales ==(len(cadena)//2):  
        print("Es capicua")
    else:
        print("No es capicua")


proceso("1331")


'''
Podemos acceder a valores negativos para acceder a valores de las estructuras de datos 
Para acceder al ultimo valor pondremos el indice -1, para el penultimo el -2 y asi hasta el primero.
lista = [1,2,3] print(lista[-1]) accedemos al valor 3, print(lista[-2]) accedemos al valor 2.

'''