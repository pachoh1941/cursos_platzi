def divide_elementos_de_lista(lista, divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e) #Esto mostraría que hay un error de "division by zero" si lo hay
        return lista


def run():
    lista = list(range(10))
    divisor = 3 

    print(divide_elementos_de_lista(lista, divisor))


if __name__=='__main__':
    run()