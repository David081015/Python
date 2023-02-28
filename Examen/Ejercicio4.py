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
  pf = ''
  cantidad=0
  for keys,values in diccionario.items():
    if values > cantidad:
      cantidad = values
      pf = keys
  print(diccionario)  
  return pf,cantidad

print(contadic(creadic()))