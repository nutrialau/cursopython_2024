#CLASE 25/6: TENIENDO DOS LISTA LA CUAL LLAMAREMOS lista_1 y lista_2 hay que hacer los siguientes ejercicios

#Añadir a la lista_1 el entero 4567 y despues el string "UNAHUR"
lista_1=[4567,'UNAHUR']
print('lista 1',lista_1)
#Añadir a la lista_2 el string "EDUCACION" y despues el entero 789
lista_2=['EDUCACION',789]
print('lista 2',lista_2)
#Crear una lista_3 con todos los elementos de la lista_1 MENOS el último
lista_3=[lista_1.pop(0)]#funcion pop para sacar el ultimo item
print('lista 3',lista_3)
#Crear una lista_4 con todos los elementos de la lista_2 MENOS el primero y último
lista_4=[lista_2[2:]]
print('lista 4',lista_4)
#Crear una lista_5 con todos los elementos de la lista_3 y de la lista_4
lista_5=[lista_3,lista_4]
print('lista 5',lista_5)



#                              AHORA CON TUPLAS
#Crear una variable llamada tupla con más de 15 items y printear lo siguiente:

# El ultimo item de la tupla creada, el numero de items de la misma, la posicion donde se encuentra algun item que haya dentro, una lista con los ultimos cuatro items de la tupla, un item que haya en la posicion 8, el numero de veces que se repite algún item dentro de la misma.

tupla=(3,5,6,7,'hola',3,-8,'mundo','hola',lista_1,lista_2,3,-5,-8,'soy posicion 15',369,-7*7,5-2)
print('el ultimo valor', tupla[-1])
print('Nro de items', len(tupla))
print('Posicion de algun item', tupla.index(6))
print('una lista con los ultimos cuatro items de la tupla',tupla[14:])
print('un item que haya en la posicion 8',tupla[8])
print(' el numero de veces que se repite algún item dentro de la misma',tupla.count(3))
