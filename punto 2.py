archivo= open("mbox.txt", "r") #Se abre el archivo
txt = archivo.read().lower() #Se convierte el texto a minúsculas para que no haya distinción entre mayúsculas y minúsculas
for char in "0123456789-_()[],.:!#$%&+-/=¿?<>¡@": #Se recorren los caracteres especiales
  txt= txt.replace(char, " ") #Se remplazan los caracteres especiales por espacios

palabras= txt.split() #Se separan las palabras por espacios
cont_palabr = [] #Se crea una lista vacía
for i in palabras: #Se recorren la lista de palabras
  encontrado:bool = False #Se inicializa la variable encontrado en falso
  for j in range(len(cont_palabr)): #Se recorre la lista de palabras contadas
    if i == cont_palabr[j][0]: #Si la palabra ya está en la lista de palabras contadas
      cont_palabr[j] = (cont_palabr[j][0], cont_palabr[j][1] + 1) #Se aumenta el contador de la palabra
      encontrado = True #Se cambia la variable encontrado a verdadero
      break #Se rompe el ciclo
  if not encontrado: #Si la palabra no está en la lista de palabras contadas  
    cont_palabr.append((i, 1))#Se agrega en una tupla la palabra y la primera vez que aparece
        
cont_palabr.sort(key=lambda x: x[1], reverse=True)  # Ordenar la lista por frecuencia en orden descendente
top_50 = cont_palabr[:50]  # Obtener los 50 primeros

# Imprimir las 50 palabras más frecuentes
for palabra, frecuencia in top_50:
    print(f"{palabra}: {frecuencia}")