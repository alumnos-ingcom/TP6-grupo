################
# Tomás Gadea - @B4zy
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def limpiar(palabra):
    palabra = palabra.lower()
    if " " in palabra:
        palabra = palabra.replace(" ","")
    if "," in palabra:
        palabra = palabra.replace(",","")
    if "–" in palabra:
        palabra = palabra.replace("–","")
    acento_a = "á"
    acento_e = "é"
    acento_i = "í"
    acento_o = "ó"
    acento_u = "ú"
    for acento_a in acento_a:
        palabra = palabra.replace(acento_a,"a")
    for acento_e in acento_e:
        palabra = palabra.replace(acento_e,"e")
    for acento_i in acento_i:
        palabra = palabra.replace(acento_i,"i")
    for acento_o in acento_o:
        palabra = palabra.replace(acento_o,"o")
    for acento_u in acento_u:
        palabra = palabra.replace(acento_u,"u")
    return palabra

def anagrama_dos(archivo): 
    for linea in archivo:
        lista_2 = linea.split(sep=" ", maxsplit = 2)
        segunda_palabra = limpiar(lista_2[2].rstrip('\n'))
        primera_palabra = limpiar(lista_2[0])
        primera_lista = list(str(primera_palabra.lower()))
        segunda_lista = list(str(segunda_palabra.lower()))
        comp_uno = sorted(primera_lista)
        comp_dos = sorted(segunda_lista)
        if comp_uno == comp_dos:
            print(f"'{primera_palabra}' y '{segunda_palabra}' son anagramas")
        else:
            print(f"'{primera_palabra}' y '{segunda_palabra}' No son anagramas")

    

def principal():
    archivo = open("anagramas.txt", "r", encoding="utf8")
    anagrama_dos(archivo)
    archivo.close()
    


if __name__ == "__main__":
     principal()


