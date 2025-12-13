# DICCIONARIOS
# Son colecciones desordenadas de elementos que se almacenan en pares clave-valor. 
# Cada clave es única y se utiliza para acceder a su valor correspondiente.
# Se definen utilizando llaves {} y los pares clave-valor se separan por comas.

capitales = {
    "Perú":"Lima",
    "Ecuador":"Quito",
    "Colombia":"Bogota",
    "Argentina":"Buenos Aires"
}

# acceder al valor de una clave
print(capitales["Ecuador"])

#agregar o modificar un nuevo clave-valor
capitales["Chile"] = "Santiago"
nueva_capital = {
    "Bolivia":"La Paz"
}

capitales.update(nueva_capital)
print(capitales)

# Eliminar un par clave-valor
del capitales['Argentina']
capital_eliminada = capitales.pop('Ecuador','NO EXISTE')
print(f'Se elimino la capital {capital_eliminada}')
print(capitales)

#recorrer un diccionario
print("Recorriendo diccionarios")
# por claves
for clave in capitales.keys():
    print(clave)
    
# por valor
for valor in capitales.values():
    print(valor)
    
# por clave valor
for clave,valor in capitales.items():
    print(f'La capital de {clave} es {valor}')