################
# Tomás Gadea - @B4zy
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def decodificador(archivo, cifrado):
    from cifrado_cesar import decodificar_cesar
    mostrar = decodificar_cesar(archivo, cifrado)
    return mostrar
   
def principal():
    import shutil, os
    from pathlib import Path
    from soporte import ingreso_entero
    archivo = input("Ingrese el nombre del archivo que desea abrir: ")
    cifrado = ingreso_entero("Ingrese el cifrado: ", "El cifrado debe ser un numero.")
    try:
        with open(archivo, 'r', encoding="utf8") as archivo_original:
            arch = archivo_original.read()
            mostrar = decodificador(arch, cifrado)
            archivo_original.close()
        with open(archivo, 'r', encoding="utf8") as archivo_original:
#             archivo_original.write(mostrar)
#             archivo_original.close()
            ruta = os.getcwd() + os.sep
            origen = ruta + archivo
            archivo = os.path.splitext(f'{archivo}')[0]+''
            destino = ruta + f'{archivo}.decode.txt'
            archivo_a = origen
            nombre_nuevo = destino
            archivo_creado = open(f'{archivo}.decode.txt', 'w')
            archivo_creado.write(str((mostrar)))
            archivo_creado.close()
            
    except FileNotFoundError as error:
        print("El archivo no se encontró. (También se debe poner el tipo de archivo (ej: archivo.txt))\n", error)

if __name__ == "__main__":
    principal()