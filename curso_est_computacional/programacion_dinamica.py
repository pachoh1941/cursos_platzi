import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError: # Se utiliza como mecanismo del flujo del programa: actúa primero, pide disculpas después
        resultado = fibonacci_dinamico(n - 1,memo) + fibonacci_dinamico(n - 2,memo) #Si está creado, entonces lo generamos...
        print(f' Resultado parcial: {resultado}','*'*10, f'n = {n}, n-1 = {n-1}, n-2 = {n-2}', '*'*10, f'memo_antes = {memo}')
        memo[n] = resultado #...y luego se guarda en el diccionario
        print(f'memo_después = {memo}')

        return resultado


if __name__ == '__main__':
    sys.setrecursionlimit(10002) #Para hacer, en este caso, 10 mil llamadas + 2 adicionales

    n = int(input('Escoge un número: '))
    # resultado = fibonacci_recursivo(n)
    resultado = fibonacci_dinamico(n)
    print(resultado)