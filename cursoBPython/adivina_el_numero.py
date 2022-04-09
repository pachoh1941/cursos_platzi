import random


def run():
    vidas = 7
    dificultad = int(input("""
Bienvenido a este juego de adivinanzas.
Escoge la dificultad.
1. Fácil.
2. Regular.
3. Difícil.
4. Brujo.
Escribe el número correspondiente: """))
    vidas -= dificultad
    if vidas == 1:
        print('Muy bien, tienes ' + str(vidas) + ' intento. ¡Vamos a jugar!')
    else:
        print('Muy bien, tienes ' + str(vidas) + ' intentos. ¡Vamos a jugar!')
    
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        vidas -= 1
        if vidas == 0:
            break
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande.')
        else:
            print('Busca un número más pequeño.') 
        numero_elegido = int(input('Elige otro número: '))
    if vidas == 0:
        print('Perdiste :(')
    else:
        print('¡Ganaste! :D')


if __name__=='__main__':
    run()