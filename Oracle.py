import cx_Oracle

# Conexión a la base de datos Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'XE') # Reemplazar "localhost" con la dirección IP del servidor de Oracle
conn = cx_Oracle.connect(user='SYSTEM', password='Castillo105.dct', dsn=dsn_tns)

# Ejecutar una consulta
cursor = conn.cursor()
cursor.execute("SELECT * FROM USUARIO")
rows = cursor.fetchall()

# Imprimir los resultados
for row in rows:
    print(row)

# Cerrar la conexión
conn.close()