
from borracho import BorrachoDeDerecha
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    pos_x = []
    pos_y = []
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        pos_x.append(campo.obtener_coordenada(borracho).x)
        pos_y.append(campo.obtener_coordenada(borracho).y)
    
    graficar_camino(pos_x, pos_y, pasos)

    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre = 'David')
    origen = Coordenada(0,0)
    distancias = []

    for _ in range(numero_de_intentos): #El guion bajo da a entender que no estamos recorriendo sino contando
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y):
    grafica = figure(title='La Pea', x_axis_label='Pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='Distancia Media')

    show(grafica)

def graficar_camino(x, y, pasos): # añadido
    grafica = figure(title='El Camino de la Pea', x_axis_label='X', y_axis_label='Y')
    grafica.line(x, y, legend= f'Camino con {pasos} pasos')

    show(grafica)

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

    graficar(distancias_de_caminata, distancias_media_por_caminata)


if __name__ =='__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 1

    main(distancias_de_caminata,numero_de_intentos,BorrachoDeDerecha)