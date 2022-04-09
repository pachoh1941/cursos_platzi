def enumeracion(numero):
    objetivo = numero
    respuesta = 0
    resultado = ''

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        resultado = f'La raíz cuadrada de {objetivo} es {respuesta}'
    else:
        resultado = f'{objetivo} no tiene una raíz cuadrada exacta'
    
    return resultado


def aproximacion(numero):
    objetivo = numero
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    resultado = ''

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        resultado = f'No se encontró la raíz cuadrada de {objetivo}'
    else:
        resultado = f'La raíz cuadrada de {objetivo} es {respuesta}'
    
        return resultado



def busqueda_binaria(numero, epsilon = 0.01):
    objetivo = numero
    bajo = 0.0
    alto = max(0.0, objetivo)
    respuesta = (alto + bajo)/2
    resultado = ''

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2
    
    resultado = f'La raíz cuadrada de {objetivo} es {respuesta}'

    return resultado


def run():
    resultado = ''
    numero = int(input("""
BIENVENIDO A LA CALCULADORA DE RAÍCES CUADRADAS

Por favor inserta un número ENTERO para calcular su raíz:

"""))

    metodo_calculo = int(input("""
BIENVENIDO A LA CALCULADORA DE RAÍCES CUADRADAS

¿Cómo crees que es la raíz de tu número?
Escoge un método de cálculo recomendado según lo siguiente:

-Escribe 1 (uno) si crees que la raíz es un número entero.
-Escribe 2 (dos) si crees que la raíz es un número racional.
-Escribe 3 (tres) si crees que la raíz es un número irracional.
-Escribe 4 (cuatro) si crees que la raíz es irracional y buscas alta precisión en tu resultado.

Escribe aquí: """))

    if metodo_calculo == 1:
        resultado = enumeracion(numero)
    if metodo_calculo == 2:
        resultado = aproximacion(numero)
    if metodo_calculo == 3:
        resultado = busqueda_binaria(numero)
    else:
        resultado = busqueda_binaria(numero, epsilon = 0.001)

    print (resultado)



if __name__=='__main__':
    run()