a=2
b=10

if a==2:
     print('a vale', a)
if b==10:
         print('y b vale:', b)
if a==2 and b==10:
    print('a vale ', a, 'y b vale ',b)
    
##_________ELSE______
numero=24
if numero >=36:
    print('el numero es mayor o igual a 36')
else:
    print('el numero es menor a 36')

##_____ELIF_____ sino, si
numero=18
if numero>=18:
    print('es un adulto')
elif numero==17:
    print('casi es mayor')
else:
    print('es menor')

dato_entrada=input('Escribi: ENTRAR, SALUDO O SALIR:').upper()
if dato_entrada=='ENTRAR':
    print('Bienvenido!')
elif dato_entrada=='SALUDO':
    print('Hola, como estas?')
elif dato_entrada=='SALIR':
    print('Te estas yendo')
else:
    print('No reconozco interaccion')
#.UPPER() Funciona para que no importe si la palabra introducida esté en mayus o minus, que el programa lo reconozca igual

""" nota=int(input('Introduce tu nota: '))
if nota>=9:
    print('Sobresaliente')
elif nota>=7:
    print('Muy bien')
elif nota>=6:
    print('Bien')
elif nota>=4:
    print('Regular')
else:
    print('Desaprobaste') """
    
nota=int(input('Introduce tu nota: '))
if nota>=9:
    print('Sobresaliente')
elif nota>=7 and nota<9:
    print('Muy bien')
elif nota>=6 and nota<7:
    print('Bien')
elif nota>=4 and nota<6:
    print('Regular')
else:
    print('Desaprobaste')

#_____________SENTENCIAS____ITERATIVAS_____ repetir, o iterar

#WHILE:

#El flujo de ejecucion de una sentencia WHILE:
# 1: Evalua la condicion devolviendo FALSE o TRUE
# 2: Si la condicion es FALSE, se sale de la sentencia WHILE y continua la ejecucion con la siguiente sentencia
# 3: Si la condicion es TRUE ejecuta cada una de las sentencias que hay en el bloque del codigo y regresa al paso 1

numero=int(input('Escribi un número: '))
while numero>0:
    print(numero)
    numero-=1
print('Terminó el conteo.')

n=0
while n<=5:
    n+=1
    print('N vale ', n)
    
#While condition
#  Instrucciones de while 
#else
#  Instrucciones de while-else
#Si no se termino con break
#  Instrucciones de while-else

chance=1
while chance<=3:
    txt=input('Escribe SI: ')
    if txt == 'SI':
        print('Ok, lo conseguiste en el intento', chance)
        break
    chance+=1
else:
    print('Has agotado tus tres intentos')
    
#BREAK es una palabra reservada para cortar un bloque de codigo.
#BREAK cierra el bucle con una condicion externa.

n=5
while n<10:
    n-=1
    if n==2:
        print('ahora n vale 2 y salimos del bucle')
        break
    print('n vale ', n)

#CONTINUE: sirve para omitir una parte del bucle en la cual se activa una condicion externa
m=0
while m<10:
    m+=1
    if m==2:
        print('Continuamos con la siguiente iteracion')
        continue
    print('m vale ', m)
    
#PASS: sirve para manejar la condicion sin que el bucle se vea afectado de ninguna manera
l=0
while l<10:
    l+=1
    if l==2:
        pass
    print('l vale ', l)
    
#FOR= "Para"// "Valor" es una variable del objeto que se esta iterando // "IN"= "en" // "lista" es la lista, tupla,etc que va a ser iterada 
lista=[1,2,3,4,5]
for valor in lista:
    print('soy un item de la lista y valgo ', valor)

lista_1=[0,1,2,3,4,5,6,7,8,9,10]
for num in lista_1:
    print('Soy el valor de la lista y valgo ', num)
    num*=5
    print('Soy un valor de la lista 1 y ahora valgo ', num)
    
indice=0
numeros=[0,1,2,3,4,5,6,7,8,9,10]
for numeros in numeros:
    numeros[indice]*=5
    indice+=1
print(numeros)

texto='Hola mundo, estoy usando FOR en Python'
for letra in texto:
    print(letra)
#FOR nos permite crear una variable dentro de un bucle sin tener que determinarla antes de usarla y solo aplica para el bloque donde está. (variable local)
texto_2=''
for letra in texto:
    texto_2=letra*2
print(texto_2)
