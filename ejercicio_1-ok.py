# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
from ast import If


numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición




if numero_1>numero_2:
    print ("el numero uno es mayor al numero dos" )
 
else:
    print("el numero dos es mayor al numero uno" )

if numero_1 > 0:
    print ("el numero uno es positivo" )
else:
    print("el numero uno es negativo o cero " ) 


if numero_1 > 0 and numero_1 <100:
    print ("el numero uno es mayor a cero y menor a cien" )
else:
     print ("el numero uno es menor a cero o mayor a cien" )  

if numero_1 <10 or numero_2> -2:
    print ("el numero uno es menor a diez y el numero dos es mayor a -2" ) 
else: 
    print ("el numero uno es mayor a 10 y el numero dos es mayor a -2 " )


