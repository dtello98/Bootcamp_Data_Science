import os
from time import sleep
"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""

dic_alumnos = {
    '12345678':{
        'nombre':'Juan Perez',
        'email' : 'juanperez@gmail.com'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR ALUMNO")
        print("=" * ANCHO)
        
        dni = input("Ingrese DNI: ")
        nombre = input("Ingrese Nombre: ")
        email = input("Ingrese Email: ")
        dic_nuevo_alumno = {
            'nombre': nombre,
            'email': email
        }
        dic_alumnos[dni] = dic_nuevo_alumno
        print("Alumno registrado existosamente")
    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR ALUMNO")
        print("=" * ANCHO)
        for dni,info in dic_alumnos.items():
            print(f"DNI : {dni}")
            print(f"Nombre : {info['nombre']}")
            print(f"Email : {info['email']}")
            print('*' * ANCHO)
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR  ALUMNO")
        print("=" * ANCHO)
        dni = input("Ingrese DNI del alumno a actualizar : ")
        if dni in dic_alumnos:
            print(f"Alumno Encontrado : {dic_alumnos[dni]['nombre']}")
            nuevo_nombre = input(f"NUEVO NOMBRE({dic_alumnos[dni]['nombre']}) : ")
            nuevo_email = input(f"NUEVO EMAIL({dic_alumnos[dni]['email']}) : ")
            if nuevo_nombre:
                dic_alumnos[dni]['nombre'] = nuevo_nombre
            if nuevo_email:
                dic_alumnos[dni]['email'] = nuevo_email
            print("ALUMNO ACTUALIZADO EXITOSAMENTE!!!")
        else:
            print('No se econtro el alumno para el DNI ingresado')
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR ALUMNO")
        print("=" * ANCHO)
        dni = input("Ingrese DNI del alumno a actualizar : ")
        if dni in dic_alumnos:
            del dic_alumnos[dni]
            print('ALUMNO ELIMINADO EXITOSAMENTE')
        else:
            print('No se econtro el alumno para el DNI ingresado')
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(1)
        break
    else:
        print("OPCION NO VALIDA...")
    
    input("Presione ENTER para continuar...")