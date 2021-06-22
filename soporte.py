#################################################
##    Acá estan todas mis funciones comunes    ##
#################################################


def ingreso_entero(mensaje_ingreso, mensaje_error):
    """
    Función que pide el ingreso de un numero entero.
    """
    while True:
        numero_ingresado = input(mensaje_ingreso)
        try:
            numero_ingresado = int(numero_ingresado)
            break
        except ValueError:
            print(mensaje_error)
    return numero_ingresado
            
def recuadro(mensaje):
    """
    Rodea el mensaje con una caja asciiart, con un ancho ajustable
    """
#   largo = len(mensaje.splitlines()) No lo voy a usar hasta saber como hacer que el mensaje tenga varias lineas
    ancho = len(mensaje)
    central = '║' + mensaje
    linea = '═'
    print('╔' + '═' * ancho + '╗')
    print(central + '' * (ancho - len(central) - 1) +  "║")
    print('╚' + linea * ancho + '╝')

def factorial(numero, es_lista):
    fact = 1
    if es_lista == True:
        lista_factorial = [1]
        for i in range(1, numero + 1):
            fact *= i
            lista_factorial.append(fact)
        return lista_factorial
    else:
        for i in range(1, numero + 1):
            fact *= i
        return fact
    
