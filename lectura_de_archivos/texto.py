archivos=open("lectura_de_archivos\\texto.txt", encoding="UTF-8")
#print(archivos.read())
linea = archivos.readline(4)
print(linea)
archivos.close()

with open("lectura_de_archivos\\texto.txt", encoding="UTF-8")  as archivo:
    print(archivo.read())