import Rectangulo as rec
#from Rectangulo import *
#from Rectangulo import Cuadrado
miRectangulo = rec.Rectangulo(5,10)
miRectangulo._ancho=16
miRectangulo._largo=10
print(miRectangulo._ancho)
print(miRectangulo._largo)
print(miRectangulo._area)
miRectangulo.CalcularArea()
print(miRectangulo._area)
print(miRectangulo.Perimetro())

miCuadrado = rec.Cuadrado(6)
print(miCuadrado.Area())
print(miCuadrado.Perimetro())