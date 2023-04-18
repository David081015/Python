import psycopg2

class Conexion:
    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "Castillo105.dct"
    _DBPORT = "2432"
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def ObtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = psycopg2.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    host = cls._HOST,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    port = cls._DBPORT,
                    database = cls._DATABASE
                )
                return cls._pool
            except Exception as e:
                print(e)
        else:
            return cls._pool
    
    def ObtenerConexion(cls):
        conexion=cls.ObtenerPool.getconn()
        return conexion
    
    def LiberarConexion(cls,conexion):
        cls.ObtenerPool().putconn(conexion)

    def cerrarConexion(cls):
        cls.ObtenerConexion().closeall()