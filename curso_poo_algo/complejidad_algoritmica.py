import time
import sys #Para mapliar el límite de recursión

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n-1)


if __name__=='__main__':
    n = 50000
    sys.setrecursionlimit(300000)

    #Aquí se mide el tiempo del primer algoritmo
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    #Aquí se mide el tiempo del segundo algoritmo
    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)