import pandas as pd
#import matplotlib as mp
file=pd.read_csv("ej2.csv")
#print(file)
file['Ventas']=file['Cantidad'] * file['Precio unitario']
#print(file)
file=file.groupby('Producto')['Precio unitario'].sum()
print(file)


