'''Automata Finito Determinista'''

class AFD:
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
        derivaciones=""
        estado_actual = self.__estado_inicial
        if(self.cadenaEnLenguaje(cadena)):
            for simbolo in cadena:
                #if simbolo not in self.__alfabeto:
                    #return False
                if (estado_actual,simbolo) in self.__transiciones:
                    # Derivaciones
                    derivaciones += f"{estado_actual}--{self.__traducir_alfabeto[simbolo]}-->{self.__transiciones[(estado_actual,simbolo)]}\n"
                    # Transicion
                    estado_actual = self.__transiciones[(estado_actual,simbolo)]
            if estado_actual in self.__estados_aceptacion:
                print("La cadena es aceptada por el automata")
                print(derivaciones)
                return True
            else:
                print("La cadena no es aceptada por el automata")
                return False
        else:
            print("La cadena presenta simbolos que no pertenecen al alfabeto")
            return False
    
    #def rutaValidacion(self):
        