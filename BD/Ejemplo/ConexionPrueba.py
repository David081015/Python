import psycopg2
from logger_base import log
conexion = psycopg2.connect(user="postgres", password="Castillo105.dct", host="127.0.0.1",port="5432",
                            database="clase_db")
log.debug(conexion)
cursor = conexion.cursor()
cursor.execute("SELECT nombre FROM cliente")
#resultados = cursor.fetchone()#regresa uno
resultados = cursor.fetchall()#regresa todos
log.debug(resultados)