from Conexion import Conexion

class Cursor:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.ObtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,typeExcep,messageExcep,detailExcep):
        if messageExcep:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.LiberarConexion(self._conexion)