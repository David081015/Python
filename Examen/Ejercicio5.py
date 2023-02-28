miLista1=[1,2,3,4,5,6,7,8,9,10]
miLista2=[11,12,13,14,15,16,17,18,19,20]
miLista3=[21,22,23,24,25,26,27,28,29,30]
miLista4=[31,32,33,34,35,36,37,38,39,40]
miLista5=[41,42,43,44,45,46,47,48,49,50]
miLista6=[51,52,53,54,55,56,57,58,59,60]
miLista7=[61,62,63,64,65,66,67,68,69,70]
miLista8=[71,72,73,74,75,76,77,78,79,80]
miLista9=[81,82,83,84,85,86,87,88,89,90]
miLista10=[91,92,93,94,95,96,97,98,99,100]
Entrada=int(input("Ingrese una posicion del 0 al 9:"))
miL=list()
miL.append(miLista1)
miL.append(miLista2)
miL.append(miLista3)
miL.append(miLista4)
miL.append(miLista5)
miL.append(miLista6)
miL.append(miLista7)
miL.append(miLista8)
miL.append(miLista9)
miL.append(miLista10)

SalidaSuma=0
for i in range(len(miL)):
    SalidaSuma+=miL[i][Entrada]
print(f'entrada:{Entrada} Salida de la suma:{SalidaSuma}')