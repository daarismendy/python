def numVal(lista):
    numeros={}
    z=''
    for  i in lista:
        suma=0
        z=str(i)
        for j in z:
            suma+=int(j)
        numeros[i]=(suma,i**2)
    return numeros

valor=numVal([21,24,36,48])
print(valor)