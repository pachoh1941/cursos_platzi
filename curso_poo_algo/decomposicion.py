
class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo' #Se diferencian privadas de públicas con "_"
        self._motor = Motor(cilindros=4)  #Se diferencian privadas de públicas con "_"
        self._transmision = Transmision('automatica',num_velocidades=6)

    def acelerar(self, tipo='despacio', revs=3000):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
            revs = 5000 #En la vida real este parámetro vendría de un sensor
        else:
            self._motor.inyecta_gasolina(3)
            revs = 3000 #En la vida real este parámetro vendría de un sensor

        self._estado = 'en_movimiento'

        self._transmision.gestionar_velociadad(revoluciones=revs)



class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self._cantidad = None

    def inyecta_gasolina(self, cantidad):
        self._cantidad = cantidad


class Transmision:

    def __init__(self, tipo, num_velocidades, velocidad_actual=1):
        self.tipo = tipo
        self._velocidades = num_velocidades
        self.velocidad_actual = velocidad_actual

    def subir_velocidad(self):
        if self.velocidad_actual == self._velocidades:
            pass
        else:
            self.velocidad_actual += 1

    def bajar_velocidad(self):
        if self.velocidad_actual == 1:
            pass
        else:
            self.velocidad_actual -= 1

    def gestionar_velociadad(self, revoluciones):
        if revoluciones > 4000:
            self.subir_velocidad
        elif revoluciones < 2000:
            self.bajar_velocidad