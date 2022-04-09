import random

def busqueda_lineal(lista, objetivo): #Este algoritmo permite encontrar un elemento en una lista
    match = False
    contador = 0

    for elemento in lista:
        contador += 1
        if elemento == objetivo:
            match = True
            break

    return [match,contador]
# Tenemos un O(n) porque la complejidad es directamente proporcional a 'lista'    


if __name__=='__main__':
    tamano_de_lista = int(input('¿De qué tamaño será la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? '))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]

    # encontrado = busqueda_lineal(lista, objetivo)
    resultado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if resultado[0] else "no está"} en la lista')
    print(f'Fueron necesarias {str(resultado[1])} iteraciones.')