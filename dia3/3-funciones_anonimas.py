#FUNCIONES ANONIMAS
#Son funciones que no tienen un nombre asociado
#Se definen con la palabra reservada lambda

def sumar(a,b):
    return a + b

sumar2 = lambda a,b: a + b

print(sumar(2,3))
print(sumar2(2,3))