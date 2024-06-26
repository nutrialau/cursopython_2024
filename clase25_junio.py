#Longitud de STR
#Funcion LEN ---> Cuenta cuantos caracteres tiene un STR 

esto_es_un_string='Hola soy un string'

print(len(esto_es_un_string))

string1='    ' #Los espacios tambien son caracteres
print(len(string1))

#Rebanar un STR---> Selecciona una parte de la cadena/STR
#Funcion SLICING----> Para hacer uso del SLICING [inicio:fin:paso]
#El inicio es el indice del primer caracter que queremos seleccionar o rebanar
#El fin es el indice del ultimo caracter NO INCLUIDO de la cadena que queremos rebanar
#El paso indica cuantos caracteres vamos a seleccionar entre las posiciones de inicio y fin

string_slicing= 'Soy un string para rebanar'
string_slicing[0:3:1]
print(string_slicing[0:3:1])

#El slicing a continuacion es para modificar un caracter especifico (en este caso el indice 1)
palabra='Pithon'
print(palabra)
print(palabra[1])

palabra=palabra[0:1]+'y'+palabra[2:]
print(palabra)

#________________Listas y Tuplas__________________ datos compuestos
mi_lista=[-11,20,3,41]
print(mi_lista)

otra_lista=['Hola,', 'como', 'estas','?']

#En Py, las listas pueden ser heterogeneas, es decir, pueden tener str e int por igual y hasta otras listas adentro

variable_1='una variable'
listita=[1,-10,132,5,'un string','otro string',variable_1]

print(listita)
print(listita[0]) #arroja el primer indice
print(listita[-1])  #Arroja el ultimo indice por indice inverso
print(listita[-2:]) #Arroja los ultimos dos indices por inverso y slicing
print(listita+[otra_lista,'ALGO RANDOM']) #Va a arrojar todo lo que esta dentro de listita, toda la otra_lista y el STR

numeros=[1,2,3,4,5,6,7,8,9,10]
print(numeros+[11,12,13,14,15,16,17,18,19,20])

numeros=[0,2,4,5,10,15,20] #como py funciona en cascada (de arriba hacia abajo), reasignamos el valor de la VAR
numeros[3]=8 #le estoy pidiendo a la lista que en el indice 3, me reemplace lo que hay por un "ocho"
print(numeros)

letras=['a','b','c','d','e','f']
letras[:3]=['A','B','C'] #le pido a la lista que me reemplace desde el inicio hasta el indice tres los STR 
print(letras) #Arroja la lista "letras" pero con los primeros tres indices en MAYÚS.
letras[:3]=[] #le pido que me muestre desde el indice tres en adelante
print(letras) #va a arrojar solo los valores siguientes al indice tres incluido

equipos=['Morón', 'Argentino Jr.','River', 'Boca', 'Independiente']
print(len(equipos))
equipos=[] #reemplazó lo que habia dentro de la lista equipos, por una lista vacia
print(equipos)

#________Funcion .APPEND___________ nos permite agregar un nuevo item al final de la lista 
colores=['rojo','verde','amarillo'] #esta es la lista
colores.append('azul') #esto es lo que va a agregar
print(colores)
#dentro del .APPEND se pueden realizar operaciones aritmeticas, es decir, si dentro del parentesis que va a agregar items le ponemos algun operador aritmetico va a arrojar el resultado cuando imprimamos

#tambien podemos utilizar la funcion LEN
print(len(colores))

#___________Funcion POP.()__________Es lo contrario a la funcion .APPEND, va a eliminar el ultimo item de una lista
colores.pop() #le pedi que elimine de la lista lo ultimo
print(colores)
#si le pongo un numero adentro del parentesis, funciona por indice y no por valores

#__________Funcion .COUNT_____________ Va a contar la cantidad de veces que algo se repite en una lista
numeros_varios=[1,2,3,5,9,12,55,20,20,20,3,5,59]
print(numeros_varios.count(20)) #.count es la funcion y entreparentesis voy a poner lo que quiero que cuente

#_________Funcion .INDEX_________ Busca el item y nos devuelve el indice en el que está
#para usarlo se escribe: nombre_de_la_lista.index(lo_que_queremos_buscar)
print(numeros_varios.index(59))


#__________TUPLAS______ son similares a las listas pero son INMUTABLES
#Se declaran con parentesis mi_tupla(1,2,3,4,5)
mi_tupla=(1,2,3,4,5)
print(mi_tupla)

otra_tupla=(1,-100,5,1,'cadena','otra cadena/string', mi_tupla,1)
print(otra_tupla)
print(otra_tupla[0]) #--->Valor unico entre parentesis por indice 
print(otra_tupla[2:]) #----> Valores por slicing
print(len(otra_tupla))
print(otra_tupla.index(5))
print(otra_tupla.count(1))
