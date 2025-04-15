
#Preguntar por una palabra y que te la devuelva al reves
'''palabra=list(input("ingrese una palabra \n"))
#for i in  reversed(range(len(palabra))):
#    print(palabra[i])
'''

#pedir palabra y letra y que devuelva cuantras veces las letras está en la palbra o frase
'''
frase=input("ingrese una frase: ")
letra=input("ingresa una letra: ")
contador=0
for i in frase:
    if i==letra:
        contador+=1

print(f"la letra está {contador} veces en la frase")
'''
#replicar lo que se escirbe hasta uqe se escriba la palabra salir
'''
while(True):
    eco=input("escriba palabra:")
    if eco=="salir":
        break
    else:
       print(eco)
'''

##### funciones#####

#decimal a binario y binario a decimall
'''
def decToBin(num):
    indice=[]
    bin=[]
    binario=[]
    comp=0
    comp2=0
    for i in range(num):
        if 2**i <= num:
            indice.append(i)
        else:
            break
    for j in reversed(indice):
        comp=2**j
        if comp==num:
            bin.append(1)
            comp2+=comp
            print(comp2)
        elif (comp<num and (comp2+comp)<=num):
            bin.append(1)
            comp2+=comp
        else: bin.append(0)  
          
    return bin        
           
  
lista=decToBin(16)
print(lista)
'''
'''
def toBin(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)
print(103%2)
'''
'''
def toDec(bin):
    lista=list(bin)
    binario=0
    for i in range(len(lista)):
        binario+=int(lista[i])*(2**i)        
    return binario
                
        
numero=toDec("0101")
print(numero)
'''
#conteo de palabras
'''
def diction(frase):
    words={}
    frase=frase.split()
    for i in frase:
        if i in words:
            words[i]+=1
        else: words[i]=1
    return words
            
                       
    
frase = input("ingrese palabra o frase")    
dicttion=diction(frase)
print(dicttion)
'''

def funcion(frase):
    frase=frase.split()
    palabras={}
    for i in frase:
        if i in palabras:
            palabras[i]+=1
        else:
            palabras[i]=1
    return palabras




def pRepet(palabra):
    valor=0
    for i in palabras:
        if valor<=palabras[i]:
            valor=palabras[i]
            valor[]=i
            
    print(f"la palabra mas repetida es {llave} valor {valor} ")
        
        
palabras=funcion("perro come perro pero no come perro")
print(f"las palabras son {palabras} y paalabras seran")
call=pRepet(palabras)
