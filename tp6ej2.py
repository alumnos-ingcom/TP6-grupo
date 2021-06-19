################
# Tomás Gadea - @B4zy
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def anagrama_dos(archivo): 
    for linea in archivo:
        lista_2 = linea.split(sep=" ", maxsplit = 2)
        segunda_palabra = lista_2[2].rstrip('\n')
        primera_palabra = lista_2[0]
        primera_lista = list(str(lista_2[0].lower()))
        segunda_lista = list(str(segunda_palabra.lower()))
        comp_uno = sorted(primera_lista)
        comp_dos = sorted(segunda_lista)
        if comp_uno == comp_dos:
            print(f"'{primera_palabra}' y '{segunda_palabra}' son anagramas")
        else:
            print(f"'{primera_palabra}' y '{segunda_palabra}' no son anagramas")

    archivo.close()

def principal():
    archivo = open("anagramas.txt", "r", encoding="utf8")
    anagrama_dos(archivo)
    


if __name__ == "__main__":
    principal()

