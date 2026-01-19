#ESCRIBIR UN ARCHIVO TXT
with open('alumnos.txt','w') as archivo:
    archivo.write("cesar mayta")
    archivo.write("\n")
    archivo.write("Carlos Perez")
    
#LEER ARCHIVO
with open('alumnos.txt','r') as archivo:
    contenido = archivo.read()
    print(contenido)
    
with open('alumnos.txt','r') as archivo:
    for linea in archivo:
        print(linea.strip())
        
#AGREGAR CONTENIDO A UN ARCHIVO EXISTENTE
with open('alumnos.txt','a') as archivo:
    nueva_linea = 'nuevo texto'
    archivo.write('\n')
    archivo.write(nueva_linea)