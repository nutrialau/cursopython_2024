#_______________________________________________________________-
#CLASE 16 de Julio, analizar el código y explicar que hace cada linea, luego reemplazarlo por otra condición
#WHILE
n = 10 #Define la variable "n"
while n<10: #(Ingresamos al bloque de codigo) Mientras que "n" sea menor a 10 se va a ejecutar el siguiente bloque
    if (n%2)==0: #En caso de que el numero sea divisible por dos (dando por resultado 0) se ejecuta el siguiente bloque
        print(n,"Es un numero par") #Imprime la variable y la frase "Es un numero par" solo cuando la condicion anterior es TRUE
    else: #En caso de que "n" sea mayor a 10, se ejecuta el siguiente bloque
        print(n,"es un numero impar") #Imprime la variable y la frase "es un numero impar" cuando la condicion del IF sea FALSE
    n+=1 #Si el valor de "n" fuera menor a 10, entonces se le suma uno, y ejecuta el bucle
    
f=int(input('Escribe un numero cualquiera: '))
while f<=100:
    if (f%7)==0:
        print(f, 'es divisible por 7')
    else:
        print(f,'NO es divisible por 7')
    f+=3
    
#  IF ELSE ELIF
# Construir un algoritmo con lo viste en clase bajo el mismo diagrama de flujo de la imagen que está en la carpeta assets del repo