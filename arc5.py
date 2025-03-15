with open("origen.txt", "r") as archivo_origen:
    contenido = archivo_origen.read()

with open("destino.txt", "w") as archivo_destino:
    archivo_destino.write(contenido)

print("El contenido se ha copiado de 'origen.txt' a 'destino.txt'.")
