# ------------------------------------------------------
# Convierte un número binario a hexadecimal.
# El número binario es un string e.g. "101":i*4+4])
        
    return numero_hexadecimal

# ----------------------------------------
# MAIN
# ----------------------------------------
if __name__ == "__main__":
    # Pide al usuario el número binario a convertir 
    # Como el número binario es un string, no hace falta usar int()
    numero_binario = input("Escribe el número en binario que quieres convertir: ")

    # se llama a la función bin2hex() para hacer la conversión
    numero_hexadecimal = bin2hex(numero_binario)

    # Muestra por pantalla el resultado.
    print("El numero binario " + numero_binario + " es " + numero_hexadecimal + " en hexadecimal.")