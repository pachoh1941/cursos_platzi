#Por "barajas" entendemos "carta" una BARAJA es una CARTA individual.
import random
import collections
from re import I

PALOS = ['picas', 'corazon', 'diamante', 'trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','J','Q','K']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor)) # Una tupla (palo, valor) es una carta

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano

# Adaptado del curso de POO--------------------------------------
def ordenamiento_de_burbuja(lista):
    carta_inicial = lista[0]
    lista_ordenada = []
    contador_lista = 0
    i_inicial = 0
    for i in range(len(VALORES)):
        if carta_inicial == VALORES[i]:
            i_inicial = i
            lista_ordenada[0] = VALORES[i_inicial]
            contador_lista += 1
            break
    
    while contador_lista < len(lista):
        if i_inicial == len(VALORES):
            i_inicial = 0
        lista_ordenada[contador_lista] = VALORES[i_inicial+contador_lista]

        #Pendiente terminar el algo
    return lista_ordenada
#--------------------------------------------------------------


def main(tamano_mano, intentos):
    barajas = crear_baraja()

    # En teoría debe haber un límite de 53 cartas
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    # Ahora vienen las distintas jugadas
    # La de la clase: PARES
    # pares = 0
    # for mano in manos:
    #     valores = []
    #     for carta in mano:
    #         valores.append(carta[1])

    #     counter = dict(collections.Counter(valores))
    #     for val in counter.values():
    #         if val == 2:
    #             pares += 1
    #             break

    # La del reto: ESCALERA COLOR

    escaleras_color = 0
    for mano in manos:
        palos = []
        valores = []
        i_inicial = 0
        cartas_en_hilo = 0
        palos_iguales = False
        for carta in mano:
            palos.append(carta[0])
            valores.append(carta[1])
        # print(palos,'*'*10, valores)
        
        for palo in PALOS: # Revisar si hay 5 palos iguales
            palos_iguales = all(carta == palo for carta in palos)
            if palos_iguales:
                print(palos_iguales,'*'*10, palo)
                break
        
        if palos_iguales:
            valores_ordenados = ordenamiento_de_burbuja(valores)
            
            for i in range(len(VALORES)):
                for j in range(len(valores_ordenados)):
                    if valores_ordenados[j] == VALORES[i]:
                        i_inicial = i
                        # print(f'i_inicial = {i_inicial}','*'*10, f'j = {j}')
                        break

            for i in range(i_inicial, len(VALORES)):
                for j in range(len(valores_ordenados)):
                    if VALORES[i] == valores_ordenados[j]:
                        cartas_en_hilo += 1 

            if cartas_en_hilo == len(valores_ordenados):
                escaleras_color += 1

            print(f'Cartas en hilo = {cartas_en_hilo}','*'*10, f'Escaleras color = {escaleras_color}')     
        
        
    # probabilidad_par = pares / intentos

    probabilidad_escalera_color = escaleras_color / intentos

    # print(f'La probabilidad para obtener un par en una mano de {tamano_mano} cartas es: {probabilidad_par}')

    print(f'La probabilidad para obtener una escalera de color en una mano de {tamano_mano} cartas es: {probabilidad_escalera_color}')


if __name__=='__main__':
    tamano_mano = int(input('¿De cuántas cartas será la mano? '))
    intentos = int(input('¿Cuántos intentos para calcular la probabilidad? '))

    main(tamano_mano,intentos)