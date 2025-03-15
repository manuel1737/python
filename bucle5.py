cadena1 = "Python es genial"
vocales = "aeiouAEIOU"
contador_vocales = sum(1 for letra in cadena1 if letra in vocales)

cadena2 = "Hola Mundo"
cadena_invertida = ""
for letra in cadena2:
    cadena_invertida = letra + cadena_invertida

cadena3 = "Hola a todos"
cadena_sin_espacios = "".join(cadena3.split())
