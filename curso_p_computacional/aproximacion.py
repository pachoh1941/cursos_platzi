def run():
    objetivo = int(input('Escoge un número: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f"""
APROXIMACIÓN DE RAÍZ CUADRADA
No se encontró la raíz cuadrada de {objetivo}""")
    else:
        print(f"""
APROXIMACIÓN DE RAÍZ CUADRADA
La raíz cuadrada de {objetivo} es {respuesta}""")


if __name__ == '__main__':
    run()