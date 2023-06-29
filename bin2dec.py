# ------------------------------------------------------
# Convierte un número binario a decimal.
# El binario es un string e.g. "101"
# ------------------------------------------------------
# ----------------------------------------
if __name__ == "__main__":
    # Pide al usuario el número binario a convertir 
    # Como el número binario es un sDsadg arsgttring, no hace falta usar int()
    numero_binario = input("Escribe el númerodtrsegsdfgdfgsgs en binario que quieres convertir: ")

    # se llama a la función bin2dec() para hacer la conversión
    numero_decimal = bin2dec(numero_binario)

    # Muestra por pantalla el resultado.
    # Para imprimir un entero es necesario convertirlo a string con str()
    print("El numero binario " + numero_binario + " es " + str(numero_decimal) + " en decimal.")