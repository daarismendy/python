def fibonacci(num):
    n=2
    fib=[0,1]
    while(True):
        fibt = fib[n-1]+fib[n-2]
        if fibt>num:      break
        else:            
            fib.append(fibt)
            n+=1           
    return fib
resultado=fibonacci(7)
print(resultado)