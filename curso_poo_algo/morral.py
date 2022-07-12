

def morral(tamano_morral,pesos, valores, n):
    
    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        print(f'El {n}-ésimo valor de los ítems es más grande que el morral:')
        print(n + '\n')
        return morral(tamano_morral, pesos, valores, n - 1)

    #Aquí viene lo más importante: escoger los artículos de mayor valor

    opcion_1 = valores[n -1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1)
    print(f'Opción 1: {opcion_1}')
    opcion_2 = morral(tamano_morral, pesos, valores, n - 1)
    print(f'Opción 2: {opcion_2}')
    return max(opcion_1, opcion_2)


if __name__=='__main__':
    valores = [60, 100, 120]
    print(f'Valores: {valores}')
    pesos = [10, 20, 30]
    print(f'Pesos: {pesos}')
    tamano_morral = 50
    print(f'Tamaño morral: {tamano_morral}')
    n = len(valores)
    print(f'n = {n}')

    resultado = morral(tamano_morral, pesos, valores, n) #Empezar desde el final: n
    print(resultado)