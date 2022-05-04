#Por "barajas" entendemos "carta" una BARAJA es una CARTA individual.
import random
import collections

PALOS = ['picas', 'corazon', 'diamante', 'trebol']
VALORES = ['as,','1','2','3','4','5','6','7','8','9','10','J','Q','K']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)

    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    # En teoría deb haber un límite de 53 carta
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    # Ahora vienen las distintas jugadas
    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break
        
    probabilidad_par= pares / intentos
    print(f'La probabilidad para obtener un par en una mano de {tamano_mano} cartas es: {probabilidad_par}')


if __name__=='__main__':
    tamano_mano = int(input('¿De cuántas cartas será la mano? '))
    intentos = int(input('¿Cuántos intentos para calcular la probabilidad? '))

    main(tamano_mano,intentos)