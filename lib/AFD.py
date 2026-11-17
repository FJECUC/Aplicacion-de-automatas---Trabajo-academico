'''Automata Finito Determinista'''

class AFD:
    def __init__(self,alfabeto:set,estados:set,estados_aceptacion:set,estado_inicial:str,transiciones:dict):
        self.__alfabeto = alfabeto
        self.__estados = estados
        self.__estados_aceptacion = estados_aceptacion
        self.__estado_inicial = estado_inicial
        self.__transiciones = transiciones

    @property
    def estados(self):
        return self.__estados
    @estados.setter
    def estados(self,estados:set):
        self.__estados = estados

    def cadenaEnLenguaje(self,cadena:str):
        for simbolo in cadena:
            if simbolo not in cadena:
                return False
        return True

    def validarCadena(self, cadena:str):
        estado_actual = self.__estado_inicial
        for simbolo in cadena:
            if simbolo not in self.__alfabeto:
                return False
            if (estado_actual,simbolo) in self.__transiciones:
                estado_actual = self.__transiciones[(estado_actual,simbolo)]
        if estado_actual in self.__estados_aceptacion:
            return True
        else:
            return False
    #def rutaValidacion(self):
        