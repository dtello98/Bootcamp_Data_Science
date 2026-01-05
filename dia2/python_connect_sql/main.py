import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='db_g6'
)

print('estas conectado a la base de datos')

cursor = connection.cursor()
cursor.execute("select nombre,email from alumno")
resultado = cursor.fetchall()
for registro in resultado:
    print('**************')
    print(f'Nombre : {registro[0]}')
    print(f'Email : {registro[1]}')
    
connection.close()