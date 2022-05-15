import random
from bokeh.plotting import figure, show#, output_file

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        #Alternativa: usar random.randint(1,7)
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    for tiro in tiros:
        if 1 not in tiro:
            tiros_con_1 += 1

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Probaibilidad de no obtener por lo menos un 1 un {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')
# Reto:
# Probabilidad de obtener un 12 tirando dos dados en por lo menos 10 tiros de ambos dados
def reto(numero_de_tiros, numero_de_intentos):
    tiros_de_dos_dados = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros_1 = tirar_dado(numero_de_tiros)
        secuencia_de_tiros_2 = tirar_dado(numero_de_tiros)
        zip_secuencias = zip(secuencia_de_tiros_1, secuencia_de_tiros_2)
        secuencia_de_dos_dados = [tiro_1 + tiro_2 for (tiro_1, tiro_2) in zip_secuencias]
        tiros_de_dos_dados.append(secuencia_de_dos_dados)

        #Gráfica de tiros dobles
        if numero_de_intentos == 1:
            fig = figure()
            x_vals = range(1,13)
            y_vals = []

            for numero in x_vals:
                repeticiones_de_numero = 0
                for tiro_doble in secuencia_de_dos_dados:
                    if numero == tiro_doble:
                        repeticiones_de_numero += 1
                y_vals.append(repeticiones_de_numero) 

            fig.line(x_vals, y_vals, line_width = 2)
            show(fig)

    tiros_con_12 = 0
    for tiro_doble in tiros_de_dos_dados:
        if 12 in tiro_doble:
            tiros_con_12 += 1

    probabilidad_tiros_con_12 = tiros_con_12 / numero_de_intentos
    print(f'Probabilidad de al menos un 12 en {numero_de_tiros} tiros dobles = {probabilidad_tiros_con_12}')


if __name__=='__main__':
    numero_de_tiros = int(input('Cuántos tiros del dado: '))
    numero_de_intentos = int(input('Cuántas veces correra la simulación: '))

    # main(numero_de_tiros, numero_de_intentos)
    reto(numero_de_tiros, numero_de_intentos)