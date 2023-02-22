#Un pizzeria ofrece pizzas vegetarianas y no vegetarianas con un listado de ingredientes.
# Ingredienes vegetarianos: pimiento y tofu
# Ingredientes no vegetarianos: pepperoni , jamon, salmon
#Escribir un programa que pregunte si quiere una pizza vegetariana o no
#en funcion a la respuesta, desplegar el menu de ingredientes, se pueden elegir maximo 2 ingredientes
#minimo 1, ademas la mozzarella y el tomate estan en todas las pizzas
#y al final se debe mostrar si la pizza es vegetariana o no y todos los ingredientes.
Salir = False
while (Salir == False):
    print("**Pizza TeLaComesEntera**\n1-Vegetariana \n2-No vegetariana \n3-Salir")
    Orden = int(input())
    Vege = "Pizza vegetariana"
    Nove = "Pizza no vegetariana"
    if Orden == 1:
        Ingr = int(input("*Ingredientes* \n1-Pimiento \n2-Tofu \n3-Ambos\n"))
        if Ingr == 1:
            print(Vege + " Ingredientes: Pimiento, Mozzarella y Tomate\n")
        elif Ingr == 2:
            print(Vege + " Ingredientes: Tofu, Mozzarella y Tomate\n")
        else:
            print(Vege + " Ingredientes: Pimiento, Tofu, Mozzarella y Tomate\n")
    elif Orden == 2:
        Ingr = int(input("*Ingredientes* \n1-Pepperoni \n2-Jamon \n3-Salmon \n4-Todo\n"))
        if Ingr == 1:
            Otro = int(input("*Otro* \n1-Jamon, \n2-Salmon, \n3-No\n"))
            if Otro == 1:
                print(Nove + " Ingredientes: Pepperoni, Jamon, Mozzarella y Tomate\n")
            elif Otro == 2:
                print(Nove + " Ingredientes: Pepperoni, Salmon, Mozzarella y Tomate\n")
            else:
                print(Nove + " Ingredientes: Pepperoni, Mozzarella y Tomate\n")

        elif Ingr == 2:
            Otro = int(input("*Otro* \n1-Pepperoni, \n2-Salmon, \n3-No\n"))
            if Otro == 1:
                print(Nove + " Ingredientes: Pepperoni, Jamon, Mozzarella y Tomate\n")
            elif Otro == 2:
                print(Nove + " Ingredientes: Jamon, Salmon, Mozzarella y Tomate\n")
            else:
                print(Nove + " Ingredientes: Jamon, Mozzarella y Tomate\n")
        
        elif Ingr == 3:
            Otro = int(input("*Otro* \n1-Pepperoni, \n2-Jamon, \n3-No\n"))
            if Otro == 1:
                print(Nove + " Ingredientes: Pepperoni, Salmon, Mozzarella y Tomate\n")
            elif Otro == 2:
                print(Nove + " Ingredientes: Jamon, Salmon, Mozzarella y Tomate\n")
            else:
                print(Nove + " Ingredientes: Salmon, Mozzarella y Tomate\n")
        
        else:
            print(Nove + " Ingredientes: Pepperoni, Jamon, Salmon, Mozzarella y Tomate\n")
    else:
        Salir = True