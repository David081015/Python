# Tipos de datos
# Una jugueteria vende dos tipos de productos payasos y muñecas, hace su venta por correo
# y la logistica le cobra por peso de cada paquete, asi que deben calcular el peso de 
# payasos y muñecas, cada payaso pesa 112, muñeca 75.

# Escribir un programa en el cual captures el numero de payasos y muñecas, calcule el peso total y precio
# total, si por cada 100 gramos de payaso se cobra 2.5 pesos y por cada 100 gramos de muñeca 2 pesos.
print("Cantidad de payasos: ")
Payaso = int(input())
print("Cantidad de muñecas: ")
Muñeca = int(input())

PesoPayaso = Payaso * 112
PesoMuñeca = Muñeca * 75

PrecioPayaso = (PesoPayaso/100)*2.5
PrecioMuñeca = (PesoMuñeca/100)*2

PesoTotal = PesoPayaso + PesoMuñeca
PrecioTotal = PrecioPayaso + PrecioMuñeca

print(f"Peso total: {PesoTotal}, Precio total: {PrecioTotal}")
