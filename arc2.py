with open("poema.txt", "r") as archivo:
    numero_lineas = sum(1 for linea in archivo)
    print(f"El archivo tiene {numero_lineas} líneas.")
