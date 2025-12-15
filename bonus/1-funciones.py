# FUNCIONES EN PYTHON
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Se define utilizando la palabra clave 'def', seguida del nombre de la función y paréntesis.

def saludar(nombre):
    mensaje = f'Hola {nombre} '
    return mensaje


usuario = input('Hola, como te llamas? ')
print(saludar(usuario))