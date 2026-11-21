class AFD:
    '''Automata Finito Determinista'''
    def __init__(self,alfabeto:set,estados:set,estados_aceptacion:set,estado_inicial:str,transiciones:dict):
        self.__alfabeto = alfabeto
        self.__estados = estados
        self.__estados_aceptacion = estados_aceptacion
        self.__estado_inicial = estado_inicial
        self.__transiciones = transiciones

    def __init__(self,alfabeto:set,estados:set,estados_aceptacion:set,estado_inicial:str,transiciones:dict, traducir_alfabeto:dict,desc_estado:dict):
        self.__alfabeto = alfabeto
        self.__estados = estados
        self.__estados_aceptacion = estados_aceptacion
        self.__estado_inicial = estado_inicial
        self.__transiciones = transiciones
        self.__traducir_alfabeto = traducir_alfabeto
        self.__desc_estado = desc_estado
        self.derivacion = ""
        self.derivacion_traducida = ""

    @property
    def estados(self):
        return self.__estados
    @estados.setter
    def estados(self,estados:set):
        self.__estados = estados

    def cadenaEnLenguaje(self,cadena:str):
        '''Validar si los simbolos de la cadena pertenecen al alfabeto'''
        for simbolo in cadena:
            if simbolo not in self.__alfabeto:
                print("La cadena presenta simbolos que no pertenecen al alfabeto")
                return False
        return True

    def actualizarDerivaciones(self,estado_actual,simbolo):
        '''Registra las derivaciones con simbolos o traducidos'''
        self.derivacion += f"{estado_actual}--{simbolo}-->{self.__transiciones[(estado_actual,simbolo)]}\n"
        self.derivacion_traducida += f"{self.__desc_estado[estado_actual]}--{self.__traducir_alfabeto[simbolo]}-->{self.__desc_estado[self.__transiciones[(estado_actual,simbolo)]]}\n"

    def validarCadena(self, cadena:str):
        '''Validar si el automata acepta la cadena'''
        self.derivacion="" #Reiniciamos las derivaciones
        self.derivacion_traducida ="" #Reiniciamos las derivaciones traducidas
        estado_actual = self.__estado_inicial
        if(self.cadenaEnLenguaje(cadena)):
            for simbolo in cadena:
                if (estado_actual,simbolo) in self.__transiciones:
                    # Registrar derivacion
                    self.actualizarDerivaciones(estado_actual,simbolo)
                    # Transicion
                    estado_actual = self.__transiciones[(estado_actual,simbolo)]
            if estado_actual in self.__estados_aceptacion:
                print("La cadena es aceptada por el automata")
                print(self.derivacion_traducida)
                print(self.derivacion)
                return True
            else:
                print("La cadena no es aceptada por el automata")
                return False
        else:
            return False


class AFND:
    def __init__(self,estados:set):
        self.estados = estados
