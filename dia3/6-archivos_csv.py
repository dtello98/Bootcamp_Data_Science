import csv

with open('alumnos.csv','w',newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['dni','Nombre','Email'])
    escritor.writerow(['45454545','Jose Perez','jperez@gmail.com'])
    
# Leer un archivo CSV
with open('alumnos.csv','r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print('----------------')
        for campo in fila:
            print(campo)
    
