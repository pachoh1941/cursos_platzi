#Librerías para graficar copmlejidad
from timeit import default_timer as timer
import random
from bokeh.plotting import figure, output_file, show


def morral(tamano_morral,pesos, valores, n):
    
    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        # print(f'El {n}-ésimo valor de los ítems es más grande que el morral:')
        # print(n + '\n')
        return morral(tamano_morral, pesos, valores, n - 1)

    #Aquí viene lo más importante: escoger los artículos de mayor valor

    opcion_1 = valores[n -1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1)
    # print(f'Opción 1: {opcion_1}')
    opcion_2 = morral(tamano_morral, pesos, valores, n - 1)
    # print(f'Opción 2: {opcion_2}')
    return max(opcion_1, opcion_2)


if __name__=='__main__':
    #Experimento para medir la complejidad:
    iteraciones = int(input('Ingresa la cantidad de veces que se repetirá el algo: '))
    resultados =[]
    tiempos = []
    VALORES = [10,20,30,40,50,60,70,80,90,100]
    PESOS = [10,20,30]
    tamanos = [(i+1) * 10 for i in range(iteraciones)]
    print(tamanos)

    for i in range(iteraciones):

        start = timer()
        valores = [random.choice(VALORES), random.choice(VALORES), random.choice(VALORES)]
        pesos = [random.choice(PESOS), random.choice(PESOS), random.choice(PESOS)]
        tamano_morral = tamanos[i]
        n = len(valores)
        resultado = morral(tamano_morral, pesos, valores, n) #Empezar desde el final: n
        end = timer()
        tiempos.append(end - start)
        resultados.append(resultado)

    #Gráfica´
    x_iteraciones = [i + 1 for i in range(iteraciones)]

    # output_file('graficado_simple.html')
    fig = figure()
    fig.line(tamanos, tiempos, line_width=2)
    show(fig)


    #Implementación única con prints para entender
    # valores = [60, 100, 120]
    # print(f'Valores: {valores}')
    # pesos = [10, 20, 30]
    # print(f'Pesos: {pesos}')
    # tamano_morral = 50
    # print(f'Tamaño morral: {tamano_morral}')
    # n = len(valores)
    # print(f'n = {n}')

    # resultado = morral(tamano_morral, pesos, valores, n) #Empezar desde el final: n
    # print(resultado)