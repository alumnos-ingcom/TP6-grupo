################
# Tomás Gadea - @B4zy
# Agustin Montiveros - @agustin-montiveros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
def hace_etiqueta(contenido, etiqueta):
    '''
    Retorna el contenido envuelto en una etiqueta como está indicado en el segundo argumento.
    La funcion llamada con contenido="Hola" y etiqueta="h1" retornará
    <h1>Hola</h1>
    '''
    etiqueta_con_contenido = "<"+etiqueta+">"+contenido+"</"+etiqueta+">"
    return etiqueta_con_contenido

    
def hace_comenta(contenido_dos):
    '''
    Retorna el contenido envuelto en las marcas de comentario HTML
    <!--  -->
    (separen las marcas del contenido con un espacio)
    '''
    comentario = "<!-- " +contenido_dos+ " -->"
    return comentario

    '''
    IMPRIME:
    <html>
    <body>
    <h1>Hola HTML</h1>
    <p>Esto es un párrafo</p>
    </body>
    </html>
    '''
def hacer_pag():  
        etiqueta = input("Ingresar etiqueta: ")
        continuacion = hace_etiqueta(resultado, etiqueta)
        print(continuacion)
        
def principal():
    contenido = ""
    etiqueta = "h1"
    encabezado = hace_etiqueta(contenido+"Hola HTML", etiqueta)
    print(encabezado)
    parrafo = encabezado + hace_etiqueta("Esto es un párrafo", "p")
    print(parrafo)
    cuerpo = hace_etiqueta(parrafo, "body")
    print(cuerpo)
    var_h1= hace_etiqueta(cuerpo, "html")
    print(var_h1)

    
        
        
    contenido_dos= input("Ingresar contenido del comentario: ")
    hace_comenta(contenido_dos)


if __name__ == "__main__":
    principal()

