def palindromo(palabra):
    palabra = palabra.replace(' ', '') # Sustituye los espacios por "null", para eliminarlos
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run(): # Como buena práctica se dejan DOS ESPACIOS entre CADA FUNCIÓN.
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palíndromo.')
    else:
        print('No es palíndromo.')


if __name__=='__main__':
    run()