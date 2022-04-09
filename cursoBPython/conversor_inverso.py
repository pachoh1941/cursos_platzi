def conversor(tipo_pesos, trm_usd):
    # Input del usuario
    pesos = float(input("¿Cuántos pesos " + tipo_pesos + " tienes?: "))
    # Conversión con 2 decimales
    usd = pesos/trm_usd
    usd = round(usd,2)
    # Convertimos el float a string para imprimir el resultado
    usd = str(usd)
    # Se imprime el resultado para el ususario
    print("Tienes $" + usd + " dólares.")

menu = """
Bienvenido al conversor de monedas 💰

1-Pesos colombianos
2-Pesos argentinos
3-Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3800)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    # Error
    print("Por favor, elige una opción dentro de las indicadas.")