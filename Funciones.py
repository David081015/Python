# def mifuncion(x):
#     return 2*x
# y = mifuncion(3)
# print(y)

# def resta(a,b):
#     return a - b
# print(resta(3,5))
# print(resta(b=10,a=2))

# def suma(a,b,c=5): #Valores por defecto
#     return a + b + c
# print(suma(0,0))
# #print(suma(0,0,4)) #Se puede cambiar C

# lista = [1,5,7,8]
# def suma(numeros):
#     total = 0
#     for n in numeros:
#         total += n
#     return total
# print(suma(lista))

# def suma(*numeros):
#     print(numeros)
#     print(type(numeros))
#     total = 0
#     for n in numeros:
#         total+=n
#     return total
# print(suma(1,2,3,4,5,6,7,8,8,8,6,5,4,5,5,4,4,2))

# def suma(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     suma = 0
#     for key, value in kwargs.items():
#         print(key,value)
#         suma+=value
#     return suma
# print(suma(b=2,c=5,a=4,Pedro=2))

# def suma(**kwargs):
#     suma = 0
#     for key, value in kwargs.items():
#         print(key,value)
#         suma+=value
#     return suma

# di = {'a':10,'b':12,'c':13}
# #suma(di) #Error
# print(suma(**di))

# def sumaMedia(a,b,c):
#     suma = a + b + c
#     media = suma/3
#     return suma, media
# print(sumaMedia(1,2,3))
# sumaResultado, sumaResultadoMedia = sumaMedia(1,2,3)
# print(sumaResultado,sumaResultadoMedia) 

# def miFuncionSuma(a,b):
#     #Comentas un mensaje para la funcion
#     """
#     Descripcion util de la funcion, como debe ser usada, que parametros etc etc
#     """
#     return a+b
# miFuncionSuma(1,2)
# # help(miFuncionSuma)#Te imprime la documentacion
# # print(miFuncionSuma.__doc__)#Te imprime la documentacion

# def multiplicar(numero:int) -> int: #Indicas que son enteros, tanto el parametro y el return
#     return numero*3
# print(multiplicar(5.8))
# print(multiplicar("5.8"))

# def funcion(a,b,*args,**kwargs):
#     print(a)
#     print(b)
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(key,value)

# funcion(10,2,5,6,4,2,3,x=4,c=7,m=10)

# numeros = list(range(1,101))
# print(numeros)
# def suma(*numeros):
#     suma = 0
#     for n in numeros:
#         suma+=n
#     return suma
# print(suma(*numeros))

# x = lambda a: print(a+10)
# x(10)

# (lambda a: print(a+10))(90) #Encerrar entre parentesis se llama la funcion,
# #se envian los parametros con otros parentesis

# (lambda *n: print(sum(n)))(*list(range(0,101,1))) #se agrega * antes de list 
# #para enviar los elementos de la list

# def multiplicador(n):
#     return lambda a: print(a*n)
# duplicador = multiplicador(2)
# duplicador(800)
# triplicador = multiplicador(3)
# triplicador(800)

# suma = None
# try:
#     #suma = 1 + "1"
#     suma = 1 + 2
# except Exception as e:
#     print(e)
# else:#Si se puede realizar hace esto
#     print(suma)
# finally:#Si o si se realiza
#     print(suma)

#ASSERT
# Luego se vera como utilizar try con assert, porque se necesita algo mas para poder ver
# def suma(a,b):
#     try:
#         assert(type(a)==int)
#         assert(type(b)==int)
#         print(a+b)
#     except AssertionError as ae:
#         print(ae)
# suma(1.2,2)
# print("fin")

def suma(a,b):
    assert(type(a)==int)
    assert(type(b)==int)
    print(a+b)
#suma(1.2,2)
suma(3,2)
print("fin")
