################
# Tomás Gadea - @B4zy
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_anagrama(primera_cadena, segunda_cadena):
    primera_lista = list(str(primera_cadena))
    segunda_lista = list(str(segunda_cadena))
    return sorted(primera_lista) == sorted(segunda_lista)


def principal():
    primer_ingreso = input("Ingrese algo: ")
    segundo_ingreso = input("Ingrese otra cosa: ")
    mostrar = es_anagrama(primer_ingreso, segundo_ingreso)
    if mostrar == True:
        print(f"'{primer_ingreso}' y '{segundo_ingreso}' son anagramas")
    else:
        print(f"'{primer_ingreso}' y '{segundo_ingreso}' NO son anagramas")

if __name__ == "__main__":
    principal()