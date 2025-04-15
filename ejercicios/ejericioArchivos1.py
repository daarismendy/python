with open("texto.txt", "r",encoding="UTF-8") as archivo:
    linea_mayor=""
    valor_anterior=0
    for i in archivo:
        linea,valor=i.split(":")
        if int(valor)>int(valor_anterior):
            valor_anterior=valor
            linea_mayor=linea
    print(f"la palabra mas frecuente es {linea_mayor} con frecuencia {valor_anterior}")
    
        

        
