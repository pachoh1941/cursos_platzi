def factorial (n):
    """Calcula el factorial de n.
    param: n int > 0
    returns: n!
    """
    print(n) #Para ver qué hace
    if n == 1:
        return 1
    return n * factorial(n-1)


def run():
    n = int(input('Escribe un entero: '))
    print(factorial(n))


if __name__ == '__main__':
    run()