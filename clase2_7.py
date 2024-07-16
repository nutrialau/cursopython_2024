#Operadores
# OPERANDO [operador] OPERANDO
#          [- / + * ]
#Operadores aritmeticos (+,-,/,*)
#Expresiones aritmeticas: 2+2, 2-2, 3/8, 9*2
#Expresiones algebraicas: radio * 3.14 (nota1+nota2)/2

#Tipo logico: BOOLEANO o BINARIO
#Es el tipo de dato mas basico de la informacion racional y representa VERDADERO O FALSO

#Negacion
#No verdadero = FALSO (FALSE)
#No falso = VERDADERO (TRUE)

#_________________OPERADORES RELACIONALES 
#Los operadores relacionales son simbolos que se usan para comparar dos valores. Si el resultado de la comparacion es correcto, la operacion va a ser considerada TRUE, de lo contrario sera FALSE.

""" print(1+1==3) """

#IGUALDAD
#El operador de igualdad sirve para preguntarle al programa si ambos operandos son iguales.
#Nos va a devolver TRUE si son iguales y FALSE si son distintos.
#Este operador se escribe con dos signos igual (==).
a=3
print(a==3)

#DESIGUALDAD O DISTINTO
#El operador DISTINTO sirve para preguntarle al programa si ambos operandos son distintos.
#Va a devolver TRUE si son distintos, y FALSE si son iguales.
#Este operador se escribe con un signo de cierre de exclamacion y un igual (!=)
print(a!=3)

#MENOR QUE
#7<3
print(7<3)
#El operador MENOR QUE sirve para preguntarle a nuestro programa si el primer operando es menor que el segundo operando 
#Nos va a dar TRUE si el primer operando es menor al segundo y FALSE si el primer operando es mayor que el segundo.
#Se escribe con un signo menor (<)

#MENOR IGUAL QUE
#El operador MENOR IGUAL que, sirve para preguntarle al programa si el primer operando es menor que el segundo operando o si ambos son iguales
#Nos va a devolver TRUE si el primero es menor o igual al segundo y FALSE si el primero es mayor que el segundo.
#Este operador se escribe con un signo menor y un signo igual (<=)
print(7<=3)
print(10<=10)

#MAYOR QUE
#El operador MAYOR QUE sirve para preguntarle a nuestro programa si el primer operando es mayor que el segundo operando.
#Nos va a devolver TRUE si el primer operando es mayor al segundo y FALSE si el primero es menor que el segundo.
#Este operador se escribe con un signo mayor (>)
print(7>6)
print(1>2)

#MAYOR IGUAL QUE
#El operador MAYOR IGUAL QUE nos sirve para preguntarle a nuestro programa si el primer operando es mayor que el segundo operando o si ambos son iguales
#Nos va a devolver TRUE si el primero es mayor o igual que el segundo y FALSE si es menor al segundo.
#Este operador se escribe con un signo mayor y un signo igual (>=)
print(7>=3)
print(10>=10)

#Podemos hacer operaciones relacionales incluso con STR
print('Hola'=='Hola')
b='Hola'
print(b[0]=='H') #Le estoy preguntando si el indice cero de 'b' es 'H' y deberia arrojar TRUE
print(b[0]=='o') #Deberia arrojar FALSE ya que el indice cero del STR 'Hola' es 'H'

#_______________________OPERADORES LOGICOS
#NOT 
#Es la negacion 
print(not True)
print(not True==False)

#CONJUNCION Y DISYUNCION
#CONJUNCION viene de conjunto, agrupa uniendo
#DISYUNCION viene de disyunto, agrupa separando

#AND
#Va a unir una o varias sentencias logicas

#VERDADERO and VERDADERO = TRUE
#VERDADERO and FALSO = FALSE
#FALSO and FALSO = FALSE
#FALSO and VERDADERO = FALSE

print(2>1 and 5>2)
print(5>25 and 20<1)

#OR
#Es disyuncion, es decir, separa.

print(2>1 or 5>4) #verdadero or verdadero = TRUE
print(2<3 or 6<3) #verdadero or falso = TRUE
print(5<1 or 7<1) #falso or falso = FALSE
print(5<1 or 5>1) #falso or verdadero = TRUE

#NORMAS DE PRECEDENCIA
#1- Terminos entre parentesis
#2- Potencia y raices
#3- Multiplicacion y division
#4- Suma y resta

d=15
e=12
print(d**e/3**e/e*d>=15 and not (d%e**2)!=0)

numero=15
a=0
a+=1 #Incrementa el valor de a uno
print(a)

b=50
b-=5 #Disminuye el valor de a cinco
print(b)