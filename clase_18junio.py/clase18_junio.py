# Numeros enteros es igual a "INT" o "LONG"
# 6448458548462L (la L representa el long)


#Numeros flotantes o FLOAT son numeros con decimales
#EJ: 0.32 ó -33.4587


#Numeros complejos o COMPLEX son los que tienen una parte imaginaria
##Ej 33.8j (la J representa el complex)


#Operadores aritmeticos (Suma, resta, multiplicacion, division, potencia, promedio)
""" Suma= +
    Resta= -
    Multiplicacion= *
    Potencia= **
    Cociente= /
    Division= //
    Promedio= % 
"""
#Procedencia de los operadores:
""" #1 Terminos entre parentesis
    #2 Potenciacion y raices
    #3 Multiplicacion y division
    #4 Suma y resta """
    #EJ.

print(15+8)

#________________String (STR) = Cadena de texto______________
""" Comillas dobles= " "
Comillas simples'' """
print('Hola mundo')

""" 
\t deja un espacio entre strings
\n salto de linea en strings """
print('string \t con espacio')
print ('string \n con salto de linea')

#____________________________Variables_______________________
# Las variables en python son como etiquetas que nos permiten hacer referencia a los datos. 
 # Por cada dato que aparece en el programa, py va a crear un objeto que lo contiene.
 # Cada objeto va a tener: #1 un identificador unico (ID)
                          #2 un tipo de dato (entero, decimal, string, etc)
                          #3 un valor (si fuera entero, un numero. si es un string las comillas y lo que diga, etc)
#  Las variables en py no guardan los datos

dni = 39487476
a = 6
print(dni)
print (a)
 # A la izq. se escribe el nombre de la variable, luego el =, y el valor a la derecha de la igualdad
 
 
 #Metodo de salida = PRINT()
 #Metodo de entrada = INPUT()
nombre = input('Hola! Escribi tu nombre:')
print('El nombre que elegiste es...:'+ nombre)

#La funcion INPUT convierte por defecto los datos de entrada en un string (es una cadena) aunque le estemos escribiendo un numero
a=15
b=22
resultado= a+b
print(resultado)

c=12
""" d=input('Introduce tu edad:')""" #Esto lo va a convertir en string y si quisiera sumar este valor, no me va a dejar porque no es un INT
d=int(input('Introduce tu edad:')) #Conversion de Tipo (type): de esta forma logramos que py nos convierta el STR en un INT
print(c+d)


#Vamos a concatenar.
cadena_de_texto='Soy cadena de texto'
anio_de_cursada='2024'
print(cadena_de_texto + anio_de_cursada)

#Vamos a concatenar.
cadena_de_texto='Soy cadena de texto'
anio_de_cursada='2024'
print(cadena_de_texto + anio_de_cursada)
#La suma de los strings lo vamos a concatenar:
#los indices vienen: 0 (el primer caracter); 1 (el segundo caracter); 2 (el tercer caracter); etc..
#los indices inversos vienen: -1 (el ultimo caracter); -2 (el penultimo caracter), etc..
#  P  Y  T  H  O  N
#  0  1  2  3  4  5 indice  
# -6 -5 -4 -3 -2 -1 indice inverso
print(cadena_de_texto[3])
