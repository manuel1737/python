palabra_buscada = input("Introduce la palabra a buscar: ")
contador = 0

with open("articulo.txt", "r") as archivo:
    for linea in archivo:
        contador += linea.lower().count(palabra_buscada.lower())

print(f"La palabra '{palabra_buscada}' aparece {contador} veces en el archivo.")
