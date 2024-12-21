import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='datag3')

print('Estas conectado a la base de datos:', connection.database)

# alumno_cursor = connection.cursor()
# alumno_cursor.execute("INSERT INTO alumno(nro_documento,nombre) VALUES('5000','Pedro')")
# connection.commit()
# print("alumno insertado")

alumno_cursor_select = connection.cursor()
alumno_cursor_select.execute("SELECT * FROM alumno")
resultado = alumno_cursor_select.fetchall()
for registro in resultado:
    print('*'*50)
    print(f'NOMBRE : {registro[2]}')

connection.close()



