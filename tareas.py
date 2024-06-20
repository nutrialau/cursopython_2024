#CLASE 18/6: CREAR UN SCRIPT EN EL QUE PODAMOS CALCULAR LA NOTA FINAL EN BASE A 5 EXAMENES, ESTOS EXAMENES EQUIVALEN A UN PORCENTAJE DE LA NOTA FINAL.

# LA NOTA NUMERO 1 CORRESPONDE AL 20% DE LA NOTA FINAL.
# LA NOTA NUMERO 2 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 3 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 4 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 5 CORRESPONDE AL 50% DE LA NOTA FINAL.

#A esto se lo suele llamar promedio ponderado: no todos los valores tienen el mismo "peso".
#Por ejemplo, dado el ejercicio de arriba me conviene sacarme una mejor nota en el examen donde la nota vale casi el 50% de la nota final.

print('Hola! Soy Calculadora de nota final.')
nota_numero_uno=int(input('Introduce tu primer nota: '))
nota_numero_dos=int(input('Introduce tu segunda nota: '))
nota_numero_tres=int(input('Introduce tu tercer nota: '))
nota_numero_cuatro=int(input('Introduce tu cuarta nota: '))
nota_numero_cinco=int(input('Introduce tu quinta nota: '))
print('Tu nota final es: ')
print(((nota_numero_uno*2)+(nota_numero_dos*1)+(nota_numero_tres*1)+(nota_numero_cuatro*1)+(nota_numero_cinco*5))/10)


