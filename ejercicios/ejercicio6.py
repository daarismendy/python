def pares(lista):
    lista2=[]
    for i in lista:
        if i%2==0: lista2.append(i)
        print(i)
    return lista2

resultado=pares([1,2,3,4,5,6,7,8])
print(resultado)