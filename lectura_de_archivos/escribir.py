#sobreescribe el archivo.
with open("lectura_de_archivos\\texto.txt","w", encoding="UTF-8")  as archivo:
    archivo.write("mira vos")
    archivo.writelines(["esta es una nueva linea\n","linea2"])