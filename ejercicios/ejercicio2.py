

cantidad=int(input("inregse numero de companeros: "))
def obterner_companeros(cantidad):
    companeros = []
    for i in range(cantidad):
        nombre = input("ingresa tu nombre ")
        edad = int(input("ingresa tu edad"))
        companero = (nombre,edad)
        companeros.append(companero)
    #organiza la lista por edad usando funciones lambda que toma el valor del elemento edad.    
    companeros.sort(key=lambda x:x[1])
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    return asistente,profesor
    
   
#devuelve el primer y ultimo valor de la lista de companeros como asesor y profesor.
companeros1 = obterner_companeros(cantidad)
print(companeros1)


