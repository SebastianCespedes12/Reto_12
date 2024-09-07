#endswith, comprueba si un string finaliza con ciertos caracteres de un string dado, retorna booleanos.
str1= "Me llamo Juan"
str1.endswith("Juan") #True
str1.endswith("Juan.") #False

#startswith, comprueba si un string inicia con ciertos caracteres de un string dado, retorna booleanos.
str2= "Adios Juan"
str2.startswith("Adios") #True
str2.startswith("A") #True
str2.startswith("Adios,") #False

#isalpha, comprueba si todos los caracteres de un string son letras, retorna booleanos
str3="Abcdefg" 
str3.isalpha() #True

str3="1Abcdefg"
str3.isalpha() #False

#isalnum, compureba si todos los caracteres de un string son alfanumericos, retorna booleanos
str4="Abc123"
str4.isalnum() #True

str4="Abc 123"
str4.isalnum() #False

#isdigit, comprueba si todos los caracteres de un string son numeros, retorna booleanos.
str5="123456"
str5.isdigit() #True

str5="Ab123 "
str5.isdigit() #False

#isspace, comprueba si todos los caracteres de un string son espacios, retorna booleanos.
str6="  "
str6.isspace() #True

str6="  a" 
str6.isspace() #False

#istitle, comprueba si todas las palabras estan capitalizadas, retorna booleanos.
str7="Cien Años De Soledad"
str7.istitle() #True

str7="Cien años de soledad"
str7.istitle() #False

#islower,comprueba si todos los caracteres estan en minuscula, retorna booleanos.
str8="1abc "
str8.islower() #True

str8="1Abc "
str8.islower() #False

#isupper, comprueba si todos los caracteres estan en mayuscula.
str9="123ABCD "
str9.isupper() #True

str9="abc123 "
str9.isupper() #False 