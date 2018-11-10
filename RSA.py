import random
from util import generar_primo
from util import ex
from util import inverso
from util import mcd


def generar_publica(fi, n):
    """Funcion que genera la llave publica a partir de la funcion de euler y n"""
    # se elige un entero e entre 2 y fi tal que sean coprimos
    e = random.randrange(2, fi)

    # se calcula el maximo comun divisor para verificar si son coprimos
    #  de no serlo se elige otro entero e hasta encontrar alguno
    g = mcd(e, fi)
    while g != 1:
        e = random.randrange(2, fi)
        g = mcd(e, fi)

    # Se regresan los valores encontrados
    return e, n


def generar_privada(e, fi, n):
    """Funcion que genera la llave privada a partir del e y fi"""
    # Se calcula el inverso multiplicativo de e
    d = inverso(e, fi)

    return d, n


def codificar(e, n, mensaje):
    """Funcion que codifica un mensaje dada la llave publica"""
    # Se toma cada caracter del mensaje y se codifica con la llave publica
    # C    =       m      ^  e (mod n)
    mensaje_codificado = [ex(ord(char), e, n) for char in mensaje]
    # Regresa la lista con los numeros que representan a cada caracter del mensaje
    return mensaje_codificado


def decodificar(d, n, mensaje_codificado):
    """Funcion que decodifica un mensaje dada la llave privada"""
    # Se toma cada numero en la lista del mensaje_codificado y se decodifica con la llave privada
    # m   =       c    ^   d (mod n)
    mensaje = [chr(ex(char, d, n)) for char in mensaje_codificado]
    # Regresa la cadena formada por los caracteres de la lista
    return ''.join(mensaje)


if __name__ == '__main__':
    """
    Integrantes:
        Maria Dadmy Nolasco Botello
        Derian Estrada
    """
    print "Algoritmo RSA\nGenerando primos..."

    while True:
        p = generar_primo()
        q = generar_primo()

        # si p y q son iguales entonces se debe encontrar otro par de numeros primos
        #  de lo contrario se rompe el ciclo
        if p != q:
            break

    print "p = ", p
    print "q = ", q

    n = p * q
    # Se calcula la funcion de Euler
    fi = (p - 1) * (q - 1)

    print "\nGenerando llaves..."
    e, n = generar_publica(fi, n)
    print "Llave publica:\ne = ", e, "\nn = ", n

    d, n = generar_privada(e, fi, n)
    print "Llave privada:\nd = ", d, "\nn = ", n

    print "\nProbando la codificacion con llave publica..."
    mensaje = raw_input("Ingresa un mensaje: ")
    print "Codificando con llave publica..."
    mensaje_codificado = codificar(e, n, mensaje)
    print "Mensaje codificado:\n", ''.join(map(lambda x: str(x), mensaje_codificado))

    print "\nProbando la decodificacion con llave privada..."
    print "Decodificando con llave privada..."
    mensaje_decodificado = decodificar(d, n, mensaje_codificado)
    print "Mensaje decodificado:\n", mensaje_decodificado
