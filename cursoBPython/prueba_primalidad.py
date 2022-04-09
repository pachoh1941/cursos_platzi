def es_primo(numero):
    if numero == 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False
        else:
            continue
    return True


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo.')
    else:
        print('No es primo.')


if __name__=='__main__':
    run()