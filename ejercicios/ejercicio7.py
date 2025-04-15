
def wordMetric(palabras):
    res=0
    diccionario={}
    for i in palabras:
        for x in i:
            res+=ord(x)
        diccionario[i]=(len(i),res)
    return diccionario

result=wordMetric(["hola","soy","pedro"])
print(result)