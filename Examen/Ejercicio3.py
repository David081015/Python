Calidad = int(input("Prueba de calidad: "))
Barra = 1
Salir = False
while(Salir == False):
    if(Calidad > Barra):
        Barra = Barra*2
    else:
        Salir = True
Resultado = Barra - Calidad
print(f"Barra: {Barra} Segmentos: {Resultado}")