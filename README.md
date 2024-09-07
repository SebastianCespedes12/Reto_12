# Reto_12

>#### 1.Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.
endswith, comprueba si un string finaliza con ciertos caracteres de un string dado, retorna booleanos.
```python
str1= "Me llamo Juan"
str1.endswith("Juan") #True
str1.endswith("Juan.") #False
```
startswith, comprueba si un string empieza con ciertos caracteres de un string dado, retorna booleanos
```python
str2= "Adios Juan"
str2.startswith("Adios") #True
str2.startswith("A") #True
str2.startswith("Adios,") #False
```
isalpha, comprueba si todos los caracteres de un string son letras, retorna booleanos
```python
str3="Abcdefg" 
str3.isalpha() #True

str3="1Abcdefg"
str3.isalpha() #False
```
isalnum, compureba si todos los caracteres de un string son alfanumericos, retorna booleanos
```python
str4="Abc123"
str4.isalnum() #True

str4="Abc 123"
str4.isalnum() #False
```
isdigit, comprueba si todos los caracteres de un string son numeros, retorna booleanos.
```python
str5="123456"
str5.isdigit() #True

str5="Ab123 "
str5.isdigit() #False
```
isspace, comprueba si todos los caracteres de un string son espacios, retorna booleanos.
```python
str6="  "
str6.isspace() #True

str6="  a" 
str6.isspace() #False
```
istitle, comprueba si todas las palabras estan capitalizadas, retorna booleanos.
```python
str7="Cien Años De Soledad"
str7.istitle() #True

str7="Cien años de soledad"
str7.istitle() #False```
```
islower,comprueba si todos los caracteres estan en minuscula, retorna booleanos.
```python
str8="1abc "
str8.islower() #True

str8="1Abc "
str8.islower() #False
```
islower,comprueba si todos los caracteres estan en minuscula, retorna booleanos.
```python
str8="1abc "
str8.islower() #True

str8="1Abc "
str8.islower() #False
```


>#### 2.Procesar el archivo y extraer:
>Cantidad de vocales 
>Cantidad de consonantes
>Listado de las 50 palabras que más se repiten
Cantidad de vocales y consonantes:
```python
archivo= open("mbox.txt", "r")
txt= archivo.read()

sum_vocal=0
sum_letras=0

for i in range(65,123):
  if i== 65 or i == 69 or i==73 or i==79 or i==85 or i ==97 or i ==101 or i==105 or i==111 or i==117 : #Si el valor ASCII es una vocal
    sum_vocal+= txt.count(chr(i)) #Se suma la cantidad de veces que aparece cada vocal
  elif i>=65 and i<=90 or i>=97 and i<=122: #Si el valor ASCII es una letra
    sum_letras+= txt.count(chr(i)) #Se suma la cantidad de veces que aparece cada letra
consonantes= sum_letras-sum_vocal #Se restan las vocales de las letras para obtener las consonantes

print(f"Vocales: {sum_vocal}")
print(f"Consonantes: {consonantes}")
```
Listado de 50 palabras que más se repiten:
```python
archivo= open("mbox.txt", "r")
txt = archivo.read().lower() #Se convierte el texto a minúsculas para que no haya distinción entre mayúsculas y minúsculas
for char in "0123456789-_()[],.:!#$%&/=¿?¡@":
  txt= txt.replace(char, " ") #Se remplacan los caracteres especiales por espacios

palabras= txt.split() #Se separan las palabras por espacios
cont_palabr = [] #Se crea una lista vacía
for i in palabras:
  encontrado = False
  for j in  range(len(cont_palabr)) :
    if i == cont_palabr[j][0]:
      cont_palabr[j] = (cont_palabr[j][0], cont_palabr[j][1] + 1)
      encontrado = True
      break
  if not encontrado :  
    cont_palabr.append((i, 1))#Se agrega en una tupla la palabra y la primera vez que aparece
        
cont_palabr.sort(key=lambda x: x[1], reverse=True)  # Ordenar la lista por frecuencia en orden descendente
top_50 = cont_palabr[:50]  # Obtener los 50 primeros

# Imprimir las 50 palabras más frecuentes
for palabra, N_veces in top_50:
    print(f"{palabra}: {N_veces}")
```
