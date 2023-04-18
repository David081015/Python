from Mascota import Mascota
from Cursor import Cursor

class MascotaDAO:
    _SELECCIONAR = "SELECT * FROM mascota ORDER BY idMascota"
    _INSERTAR = "INSERT INTO mascota(nombre,raza,edad) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE mascota set nombre=%s,raza=%s,edad=%s WHERE idMascota=%s"
    _ELIMINAR = "DELETE FROM mascota WHERE idMascota=%s"
    _BUSCAR = "SELECT * FROM mascota WHERE edad > 10"
    _RAZA = "SELECT * FROM mascota WHERE raza = %s"