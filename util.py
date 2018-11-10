from random import randint
from random import getrandbits


def jacobi(a, n):
    # int ans;

    if a == 0:
        # a if condition else b
        # ans = (n == 1) ? 1 : 0;
        ans = 1 if n == 1 else 0
    elif a == 2:
        modulo = n % 8
        if modulo == 1 or modulo == 7:
            ans = 1
        elif modulo == 3 or modulo == 5:
            ans = -1

    elif a >= n:
        ans = jacobi(a % n, n)
    elif a % 2 == 0:
        ans = jacobi(2, n)*jacobi(a/2, n)
    else:
        ans = -jacobi(n, a) if (a % 4 == 3 and n % 4 == 3) else jacobi(n, a)
    return ans


def inverso(a, m):
        c1 = 1
        c2 = -(m // a)  # coeficiente de a y b respectivamente
        t1 = 0
        t2 = 1  # coeficientes penultima corrida
        r = m % a  # residuo, asignamos 1 como condicion de entrada
        x = a;
        y = r;
        while r != 0:
            c = x // y  # cociente
            r = x % y  # residuo
            # guardamos valores temporales de los coeficientes
            # multiplicamos los coeficiente por -1*cociente de la division
            c1 *= -c
            c2 *= -c
            # sumamos la corrida anterior
            c1 += t1
            c2 += t2
            # actualizamos corrida anterior
            t1 = -(c1 - t1) // c
            t2 = -(c2 - t2) // c
            x = y
            y = r

        if x != 1:  # residuo anterior es 1 , son primos relativos y el inverso existe
            return None

        return (m + t2) % m if t2 < 0 else t2


def ex(a, b, m):
    r = 1
    while (b):
        if (b & 1):
            r = (r * a) % m
        b >>= 1
        a = ((a % m) * (a % m)) % m
    return r


def solovay_strassen(n, k):
    # Si el numero es par, entonces no es primo
    if n % 2 == 0: return False

    for i in range(k):
        # Se obtiene un b aleatorio tal que 0 < b < n
        b = randint(1, n - 1)

        # Se calcula la primera parte de (2)
        primera = ex(b, (n - 1) // 2, n)

        # Se calcula la segunda parte de (2)
        segunda = jacobi(b, n) % n

        # Si ambas partes no son congruentes, entonces el numero es compuesto
        if primera != segunda:
            return False

    # Si se terminaron las k iteraciones, entonces muy probablemente n sea primo
    return True


def generar_primo():
    for i in range(10000000):
        posible = getrandbits(350)

        if solovay_strassen(posible, 10):
            return posible
    return None
