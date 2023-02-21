#Escribir un programa en el cual se pida una frase y una letra, escribir en pantalla el numero de 
#veces que se repita la letra
Frase = input("Introduce frase: ")
Letra = input("Introduce letra: ")
contador = 0
for i in Frase:
    if i == Letra:
        contador +=1
print("La letra '%s' aparece %2i veces en la frase '%s',"%(Letra, contador,Frase))