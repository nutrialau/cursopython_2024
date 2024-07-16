#Inicio - Interaccion 1 - Interaccion 2 - Interaccion 3 - Fin. 

#Sentencia de control 
#Dos tipos = Control y Control Iterativo

#Las sentencias de control de flujo condicionales, se van a definir por el uso de tres palabras claves reservadas: 
#If, Elif, Else.
#IF: Sí
#ELIF: Sino, si
#ELSE: Sino

#SENTENCIA IF:
#Nos permite controlar el flujo de un programa y dividir la ejecucion en diferentes caminos 
#Al utilizar esta palabra reservada le vamos a decir a Py que queremos ejecutar un bloque de codigo solo si se cumple determinada condicion, es decir, si el resultado es true.

edad=int(input('Qué edad tenés?: '))
if edad >=18: #Indentacion: indica que es un bloque de codigo (los dos puntos me indican la indentacion)
    print('Sos adulto')
if False:
    print('IMPRIMIME LA CONDICION VERDADERA')