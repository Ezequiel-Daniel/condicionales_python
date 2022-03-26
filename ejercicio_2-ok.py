# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
from ast import If


texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if texto_1 > texto_2 :
    print("la palabra uno es mayor a la palabra dos" )

else:
    print("la palabra dos es mayor a la palabra uno" )


if len(texto_1) > len(texto_2):
    print ("el texto uno tiene mas letras que el texto dos")
else:
    print("el texto dos tiene mas letras que el texto uno")

 
if (texto_1[0])>(texto_2[0]):
    print ("la primera letra de la primera palabra es mayor a la primera letra de la segunda palabra")
else: 
    print("la primera letra de la primera palabra es menor a la primera letra de la segunda palabra")


