################
# Tomás Gadea - @B4zy
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import shutil, os

        
def principal():
    ruta = os.getcwd() + os.sep
    origen = ruta + 'plantilla.py'
    destino = ruta + 'tp6ejX.py'#------>CAMBIAR LA X POR EL N° DEL EJERCICIO DESEADO

    if os.path.exists(origen):
        with open(origen, 'rb') as archivo_origen:
            with open(destino, 'wb') as archivo_destino:
                shutil.copyfileobj(archivo_origen, archivo_destino)
                print("Archivo copiado")

if __name__ == "__main__":
    principal()

