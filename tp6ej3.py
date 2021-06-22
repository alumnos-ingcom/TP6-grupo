################
# Tomás Gadea - @B4zy
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import shutil, os

        
def principal():
    ruta = os.getcwd() + os.sep #busca la ruta de los archivos con esos metodos
    origen = ruta + 'plantilla.py'  #da la ruta del archivo origen mas el nombre del archivo origen
    destino = ruta + 'tp6ejX.py'#------>CAMBIAR LA X POR EL N° DEL EJERCICIO DESEADO, da la ruta del archivo destino + el nombre del archivo destino

    if os.path.exists(origen): #da true para que el if funcione, es si existe
        with open(origen, 'rb') as archivo_origen: #abre el archivo como archivo_origen
            with open(destino, 'wb') as archivo_destino: #abre el archivo destino
                shutil.copyfileobj(archivo_origen, archivo_destino) #copia el contenido de un archivo origen al archivo destino
                print("Archivo copiado") #avisa que se copio el archivo

if __name__ == "__main__":
    principal()

