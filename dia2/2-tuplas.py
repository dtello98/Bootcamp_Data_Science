# las tuplas son inmutables
dias = ("Lunes","Martes","Miércoles","Jueves","Viernes")
print(f"Tipo de dato original : {type(dias)}")
dias = list(dias)
print(f"Tipo de dato modificado : {type(dias)}")
dias.append("Sábado")
dias = tuple(dias)

print(dias)