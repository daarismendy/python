import random
Cuestionario={"el sol es amarillo":"v","el perro es bipedo":"f","los pollos son amarillos siempre":"f"}


while(True):
    pregunta=random.choice(list(Cuestionario.keys()))
    respuesta_correcta=Cuestionario[pregunta]
      
    respuesta=input(f"ingrese v o f {pregunta}")
    
    if respuesta.lower()==respuesta_correcta.lower():
        print("correcto")
    elif respuesta=="salir":
        print("cerrando Cuestionaro")
        break
    else:
        print("incorrecto")
            

    


