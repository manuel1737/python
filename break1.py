contrasena_correcta = "python123"

while True:
    contrasena = input("Introduce la contraseña: ")
    if contrasena == contrasena_correcta:
        print("¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
