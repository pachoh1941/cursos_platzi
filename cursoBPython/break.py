def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    # Desafío - Impresor de primeros 10 divisores
    saludo = """
    Bienvenido al impresor de DIVISORES ENTREROS. 🤓🤓
    Este programa te muestra los primeros n divisores enteros de un número igualmente entero. 
    Escribe el número del que quieras saber sus primeros n divisores:
    """
    FACTOR = int(input(saludo))
    n = int(input('Escribe el número de divisores que quieres ver: '))
    divisor = 1
    contador = 0
    while contador < n:
        if FACTOR < divisor and contador < n:
            print('Has llegado al límite de divisores de tu número.' + 'Son ' + str(contador) + '.')
            break
        elif FACTOR%divisor != 0 or FACTOR/divisor < 1:
            divisor += 1
            continue
        else:
            print(divisor)
            contador += 1
            divisor += 1


if __name__ == '__main__':
    run()