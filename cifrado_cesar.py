################
# Tomás Gadea - @B4zy
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################



def codificar_cesar(texto, cifrado):
    texto = list(texto)
    texto_cesar = []
    for i in range(len(texto)):
        numero = ord(texto[i])
        numero_cifrado = numero + cifrado
        letra_cifrada = chr(numero_cifrado)
        texto_cesar.append(letra_cifrada)
    return "".join(texto_cesar)

def decodificar_cesar(texto, cifrado):
    texto = list(texto)
    texto_cesar = []
    for i in range(len(texto)):
        numero = ord(texto[i])
        numero_cifrado = numero - cifrado
        letra_cifrada = chr(numero_cifrado)
        texto_cesar.append(letra_cifrada)
    return "".join(texto_cesar)