tiempo_promedio = 0.5
tiempo_dalto=0.5-(0.5*0.3)
frase = input("ingresa una frase")
frase=frase.split() 

tiempo_de_duracion=len(frase)*tiempo_promedio
tiempo_duracion_dalto=len(frase)*tiempo_dalto
if(tiempo_de_duracion>10):
    print("para flaco")
    print(f"dalto lo diria en:{tiempo_duracion_dalto} ")
else:
    print(f"el tiempo de duracion para esta fraese es: {tiempo_de_duracion} segundos")
    print(f"dalto lo diria en:{tiempo_duracion_dalto} ")