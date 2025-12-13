dias = ["Lunes","Martes","Miércoles","Jueves","Viernes"]

# mostrar info de la lista
print(dias[0])

# agregar elementos a lista
dias.append("Sábado")
dias.append("Domingo")

# eliminar elementos de la lista
del dias[0:2]

# actualizar un valor de la lista
dias[-1] = "Lunes"

# mostrar todos los valores de la lista
for dia in dias:
    print(dia)