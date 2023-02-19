#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra
#que contiene y su frecunecia. Escribir otra funcion que reciba el diccionario y devuelva una tupla
#con la palabra mas repetida y su frecuencia
def creadic():
  cadena=input('Escriba su cadena de caracteres: ')
  Lista= cadena.split()
  dic={}
  for i in Lista:
    if i in dic:
      dic[i] +=1
    else:
      dic[i]= 1
  return dic

def contadic(diccionario):
  pf= ''
  cantidad=0
  for keys,values in diccionario.items():
    if values > cantidad:
      cantidad= values
      pf= keys
  print(diccionario)  
  return pf,cantidad

print(contadic(creadic()))