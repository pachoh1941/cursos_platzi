pesos = input("¿Te quieres vacunar en Florida? hmmm ... ¿Cuántos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
# Usamos round para quitarle decimales
dolares = round(dolares, 2)
if dolares >= 400:
    dolares = str(dolares)
    print("¡Felicidades! Tienes $" + dolares + " dólares. Te puedes vacunar con Janssen, tienes suficiente para ir y volver y ponerte una dosis.")
else:
    dolares = str(dolares)
    print("Raios :( No te alcanza para ir a vacunarte. Tienes $" + dolares + " dólares.")
