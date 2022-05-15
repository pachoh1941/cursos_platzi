import random
import math
from estadisticas import desviacion_estandar, media
from bokeh.plotting import figure, show#, output_file

def aventar_agujas(numero_de_agujas, numero_de_intentos):
    adentro_del_circulo = 0
    x_vals = []
    y_vals = []

    for _ in  range(numero_de_agujas):
        x = random.random() * random.choice([-1,1])
        y = random.random() * random.choice([-1,1])
        distancia_desde_el_centro = math.sqrt(x**2 + y**2)

        if distancia_desde_el_centro <= 1:
            adentro_del_circulo += 1
            x_vals.append(x)
            y_vals.append(y)

    #Gráfica PI
    if numero_de_intentos == 1:
        fig = figure()
        fig.scatter(x_vals, y_vals)
        show(fig)

    return (4 * adentro_del_circulo) / numero_de_agujas

def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas, numero_de_intentos)
        estimados.append(estimacion_pi)

    media_estimados = media(estimados)
    sigma = desviacion_estandar(estimados)
    print(f'Est={round(media_estimados, 5)}, sigma={round(sigma, 5)}, agujas = {numero_de_agujas}')

    return(media_estimados, sigma)

def estimar_pi(precision, numero_de_intentos):
    numero_de_agujas = 1000
    sigma = precision
    
    while sigma >= precision/1.96:
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2

    return media


if __name__=='__main___':
    numero_de_intentos = int(input('Ingresa el número de intentos: '))
    estimar_pi(0.01, numero_de_intentos)