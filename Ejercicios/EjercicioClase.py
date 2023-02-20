import Clases as C
miCuenta = C.Cuenta
miJoven = C.Joven

miCuenta("David", 1000)
miCuenta.Titular("David Castillo")
miCuenta.Ingresar(500)
print(miCuenta.Cantidad())
miCuenta.Retirar(500)
miCuenta.Mostrar()

miJoven("Sofia", 19, 1500, 2.0)
miJoven.Retirar(100, 18)
miJoven.Mostrar()