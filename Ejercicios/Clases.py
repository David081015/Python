# Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
# titular (que es una persona) y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:

# Un constructor, que reciba los parámetros para inicializar los atributos.
# Los métodos de acceso (set,get) para cada uno de los atributos. 
# El atributo cantidad no se puede modificar directamente, sólo ingresando o retirando dinero.
# mostrar(): Devuelve los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
# no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

# Definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven 
# que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar 
# una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:

# Un constructor.
# Los métodos de acceso (set,get) para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
class Cuenta:
    def __init__(self,titular="",cantidad=0) -> None:
        self._titular = titular
        self._cantidad = cantidad

    @property
    def Titular(self):
        return self._titular 
    @Titular.setter
    def Titular(self,titular):
        self._titular=titular
            
    @property
    def Cantidad(self):
        return self._cantidad
    
    def Ingresar(self, ingresar):
        Cantidad = self.Cantidad
        Cantidad += int(ingresar)
        self._cantidad = Cantidad
    
    def Retirar(self, retirar):
        self._cantidad -= retirar

    def Mostrar(self):
        return (f"Titular: {self._titular}, Cantidad: {self._cantidad}")

class Joven(Cuenta):
    def __init__(self, titular="", edad=0, cantidad=0, bonificacion=0.0) -> None:
        super().__init__(titular, cantidad)
        self._edad = edad
        self._bonificacion = bonificacion

    @property
    def Edad(self):
        return self._edad 
    @Edad.setter
    def Edad(self,edad):
        if edad < 18:
            print("Edad no valida")
        else:
            self._edad=edad
    
    @property
    def Bonificacion(self):
        return self._bonificacion 
    @Bonificacion.setter
    def Bonificacion(self,bonificacion):
        self._bonificacion=bonificacion
    
    def Retirar(self, retirar, edad):
        if edad >= 18 and self._cantidad > retirar:
            return super().Retirar(retirar)
        else:
            return ("Su edad o el retiro es invalido")
    def Mostrar(self):
        return (f"Cuenta Joven \nTitular: {self._titular}, Edad: {self._edad}, Cantidad: {self._cantidad}, Bonificación: {self._bonificacion}")