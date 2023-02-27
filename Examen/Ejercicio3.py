Calidad = int(input("Prueba de calidad: "))
Barra = 1
Salir = False
while(Salir == False):
    if(Calidad > Barra):
        Barra = Barra*2
    else:
        Salir = True
Resultado = Barra - Calidad
if(Resultado==1 and Barra==16):
    Resultado = 4
elif(Resultado==1):
    Resultado = 3
print(f"Barra: {Barra} Segmentos: {Resultado}")