import Clases as C

miCuenta = C.Cuenta("David", 1000)
miJoven = C.Joven("Sofia", 2000, 19, 2.0)

miCuenta.Titular = "David Castillo"
miCuenta.Ingresar(500)
print(miCuenta.Cantidad)
miCuenta.Retirar(500)
print(miCuenta.Mostrar())


print(miJoven.Cantidad)
miJoven.Retirar(100, 18)
print(miJoven.Mostrar())