nombres = ["Ana", "Luis", "Pedro", "María"]

with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

print("Los nombres se han guardado en 'nombres.txt'.")
