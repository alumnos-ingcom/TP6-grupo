################
# Tomás Gadea - @B4zy
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def codificador(archivo, cifrado):
    from codificador_cesar import codificar_cesar
    mostrar = codificar_cesar(archivo, cifrado)
    return mostrar
   
def principal():
    import os
    from pathlib import Path
    from soporte import ingreso_entero
    archivo = input("Ingrese el nombre del archivo que desea abrir: ")
    cifrado = ingreso_entero("Ingrese el cifrado: ", "El cifrado debe ser un numero.")
    try:
        with open(archivo, 'r', encoding="utf8") as archivo_original:
            arch = archivo_original.read()
            mostrar = codificador(arch, cifrado)
            archivo_original.close()
        with open(archivo, 'w', encoding="utf8") as archivo_original:
            archivo_original.write(mostrar)
            archivo_original.close()
            ruta = os.getcwd() + os.sep
            origen = ruta + archivo
            archivo = os.path.splitext(f'{archivo}')[0]+''
            destino = ruta + f'{archivo}.cesar.txt'
            archivo_a = origen
            nombre_nuevo = destino
            os.rename(archivo_a, nombre_nuevo)
            
    except FileNotFoundError as error:
        print("El archivo no se encontró. (También se debe poner el tipo de archivo (ej: archivo.txt))\n", error)

if __name__ == "__main__":
    principal()