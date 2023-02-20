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
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., 
# por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
class Cuenta:
    def __init__(self,titular,cantidad) -> None:
        self._titular = ""
        self._cantidad = "0"

    @property
    def Titular(self):
        return self._titular 
    Titular.setter()

    @property
    def Cantidad(self):
        return self._cantidad
    
    def Ingresar(self, ingresar):
        self._cantidad += ingresar
        return ("Se ingreso con exito")
    
    def Retirar(self, retirar):
        self._cantidad -= retirar
        return ("Se retiro con exito")

    def Mostrar(self):
        return (f"Titular: {self._titular}, Cantidad: {self._cantidad}")