class Persona:
    def __init__(self,nombre,edad) -> None:
        self._nombre = nombre
        self._edad=edad

    def __str__(self) -> str:
        return f'Persona: {self._nombre}, Edad: {self._edad}'

class Puesto:
    def __init__(self,sueldo) -> None:
        self._sueldo=sueldo

class Empleado(Persona,Puesto):
    def __init__(self, nombre, edad,puesto,sueldo) -> None:
        super().__init__(nombre, edad)
        Puesto.__init__(self,sueldo)
        self._puesto=puesto
    def __str__(self) -> str:
        return f"{super().__str__()}, Puesto: {self._puesto}, Sueldo: {self._sueldo}"
