
class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

        print('Has creado un rectángulo')

    def area(self):
        return self.base*self.altura

class Cuadrado(Rectangulo): #Se lee: la clase Cuadrado extiende a Rectángulo

    def __init__(self,lado):
        super().__init__(lado,lado) #Permite obtener referencia directa de la superclase


if __name__=='__main___':
    print('Ejecutando')
    rectangulo = Rectangulo(3,4)
    print(rectangulo.area())

    cuadrado = Cuadrado(5)
    print(cuadrado.area())