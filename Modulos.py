import random #puedes asignar un nombre con as + nombre
import csv #para excel

# numRandom = random.randint(0,100)
# while True:
#     num = int(input("Cual sera el numero entre 0 y 100?"))
#     if numRandom == num:
#         break;
#     if numRandom > num:
#         print("El numero es mayor")
#     else: 
#         print("El numero es menor")
# print("El numero era",num)

with open('Subnetting_ClassC_19100158') as file:
    reader = csv.reader(file)
    for row in reader:
        print(','.join(row))