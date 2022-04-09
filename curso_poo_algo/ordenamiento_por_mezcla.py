import random

def ordenamiento_por_mezcla(lista):

    if len(lista) > 1:
        # PARTE 1 - CRECIMEINTO LOGARÍTMICO O(log n)
        print('PARTE 1')
        # print(f'recursividad izquierda {recur_i}')
        # print(f'recursividad derecha {recur_j}')

        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda,'*'*5,derecha)

        #Llamada recursiva en cada mitad
        
        # recur_i += 1
        ordenamiento_por_mezcla(izquierda)
        
        # recur_j += 1
        ordenamiento_por_mezcla(derecha)
                

        #PARTE 2 - CRECIMIENTO ¿?
        print('PARTE 2')
        # print(f'recursividad izquierda {recur_i}')
        # print(f'recursividad derecha {recur_j}')
        i = 0
        j = 0
        #Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print(len(izquierda),len(derecha))
        print('-'*50)

        return lista
            


if __name__=='__main__':
    tamano_de_lista = int(input('¿De qué tamaño será la lista? '))
    
    # lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    lista = [6,3,1,4]
    print(lista)
    print('-'*20)

    # recur_i = 0 # contador de llamada recursiva lista izquierda
    # recur_j = 0 # contador de llamada recursiva lista derecha

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)