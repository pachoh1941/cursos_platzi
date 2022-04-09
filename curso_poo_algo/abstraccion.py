
# class Lavadora:

#     def __init__(self):
#         pass

#     def lavar(self, temperatura='caliente'):
#         self._llenar_tanque_de_agua(temperatura)
#         self._anadir_jabon()
#         self._lavar()
#         self._centrifugar()

#     def _llenar_tanque_de_agua(self, temperatura):
#         print(f'Llenando el tanque con agua {temperatura}')

#     def _anadir_jabon(self):
#         print('Anadiendo jabon')

#     def _lavar(self):
#         print('Lavando la ropa')

#     def _centrifugar(self):
#         print('Centrifugando la ropa')


#Reto:
class Televisor:

    def __init__(self,input,canales):
        self._estado_actual = 'OFF'
        self.input = input
        self.__canal = None
        self.__canales = canales
        self._inputs_posibles = ['TV','HDMI1','HDMI2']
        # self._canales_posibles = range(0,100)


    def encender_tv(self):
        self._estado_actual = 'ON'
        print(self._estado_actual)
        print('Bienvenido a tu TV')
        # while self._estado_actual=='ON':
        #     self.cambiar_input()
            
        #     if self.input == 'TV':
        #         self.cambiar_canal()
        #     else:
        #         pass
            
        #     self.estado_actual=input('Boton ON/OFF: ')

    def apagar_tv(self):
        self._estado_actual = 'OFF'

    def cambiar_input(self): #A futuro meter encapsulamiento
        try:
            if self._estado_actual == 'OFF':
                raise SystemError(f'El televisor está {self._estado_actual}. No se puede cambiar input')
            _seleccion_del_usuario = input(f"""
Seleciona tu input:
        {self._inputs_posibles[0]}
        {self._inputs_posibles[1]}
        {self._inputs_posibles[2]}
""")
            if _seleccion_del_usuario == "":
                pass
            else:
                self.input = _seleccion_del_usuario
            
            print(f'Estás en {self.input}')
        except SystemError as se:
            print (se)
            

    @property
    def canal(self): #A futuro traer error si está apagado
        return self.__canal

    @canal.setter
    def cambiar_canal(self,canal):
        if canal in self.__canales:
            self.__canal = canal
            print(f'Estás en el canal {canal}.')
        else:
            raise ValueError(f'El canal {canal} no se encuentra en tu paquete de televisión')
        #_seleccion_del_usuario = input('Seleciona tu canal: ')
        # if _seleccion_del_usuario == None:
        #     pass
        # else:
        #     try:
        #         if _seleccion_del_usuario not in self._canales_posibles:
        #             raise ValueError("El canal no existe")

        #         print(f'Estás en {self.canal}')
        #     except ValueError as ve:
        #         print(ve)


if __name__=='__main__':
    # lavadora = Lavadora()
    # lavadora.lavar()
    canales = range(0,100)
    tv = Televisor('TV', canales)
    tv.encender_tv()
    #tv.cambiar_canal = 200
    tv.cambiar_canal = 50
    tv.apagar_tv()
    tv.cambiar_input()
