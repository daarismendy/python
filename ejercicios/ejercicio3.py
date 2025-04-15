#dar un numero y encontrar todos los primos hasta el

def es_primo(num):
    for i in range(2,num-1):
        
        if num%i==0: return False
            
    return True

   
def primos_hasta(num):
    primos = []
    for i in range(1,num+1):
        if es_primo(i)==True:
            primos.append(i)
    return primos   
                    
                                
resultado = primos_hasta(26)
print(resultado)
