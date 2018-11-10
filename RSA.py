import random
from util import generar_primo
from util import ex
from util import inverso
from util import mcd


def generate_keypair(p, q):
    if p == q:
        raise ValueError('p and q cannot be equal')

    # 1) n = p*q
    n = p * q

    # 2) Calculate Euler fucntion (Phi is the coefficient of n)
    phi = (p - 1) * (q - 1)

    # 3) Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # 3.1) Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = mcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = mcd(e, phi)

    # 4) Use Extended Euclid's Algorithm to generate the private key
    d = inverso(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


'''
Encrypting a message
'''


def codificar(pk, mensaje):
    """Funcion que codifica un mensaje dada la llave publica"""
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    # C    =       m      ^  e (mod n)
    mensaje_codificado = [ex(ord(char), key, n) for char in mensaje]
    # Return the array of bytes
    return mensaje_codificado


def decodificar(d, n, mensaje_codificado):
    """Funcion que decodifica un mensaje dada la llave privada"""
    # Se toma cada numero en la lista del mensaje_codificado y se decodifica con la llave privada
    # m   =       c    ^   d (mod n)
    plain = [chr(ex(char, d, n)) for char in mensaje_codificado]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print "RSA Encrypter/ Decrypter"
    p = generar_primo()
    q = generar_primo()
    print "Generating your public/private keypairs now . . ."
    public, private = generate_keypair(p, q)
    print "Your public key is ", public, " and your private key is ", private
    message = raw_input("Enter a message to encrypt with your private key: ")
    encrypted_msg = codificar(private, message)
    print "Your encrypted message is: "
    print ''.join(map(lambda x: str(x), encrypted_msg))
    print "Decrypting message with public key ", public, " . . ."
    print "Your message is:"
    print decodificar(public[0], public[1], encrypted_msg)