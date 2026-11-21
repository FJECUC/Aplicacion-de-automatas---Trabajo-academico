from lib import AF
import os

def cls():
    '''Limpiar la consola'''
    os.system('cls')
def readCadenas(archivo):
    '''Leer cadenas del archivo escogido'''
    try:
        lineas_raw = open(archivo,"r")
        lineas = lineas_raw.readlines()
        cadena = []
        for linea in lineas:
            cadena.append(linea.removesuffix("\n"))
        return cadena
    finally:
        lineas_raw.close()

def AFDCaso1():
    '''Automata para el caso 1'''
    def setAFData():
        '''Crear los datos del automata'''
        global alfabeto
        global traducir_alfabeto
        global estados
        global desc_estado
        global estado_inicial
        global estados_aceptacion
        global transiciones
        alfabeto = ('a','b','c','d','e','f','g')
        traducir_alfabeto = {"a": "tarjeta",
                            "b": "pinOK",
                            "c": "pinMal",
                            "d": "retirar",
                            "e": "saldo",
                            "f": "confirmar",
                            "g": "cancelar"}
        estados = ('q0','q1')
        desc_estado = {'q0':'Esperando tarjeta',
                    'q1':'Esperando PIN (1er intento)',
                    'q2':'Esperando PIN (2do intento)',
                    'q3':'Esperando PIN (3er intento)',
                    'q4':'Escoger operacion',
                    'q5':'Retiro',
                    'q6':'Operacion completada|Entregar recibo|Entregar dinero|Devilver tarjeta',
                    'q7':'Tarjeta bloqueada/retenida',}
        estado_inicial = 'q0'
        estados_aceptacion = ('q7','q6')
        transiciones = {('q0','a'):'q1',
                        ('q1','b'):'q4',
                        ('q1','c'):'q2',
                        ('q1','g'):'q6',
                        ('q2','b'):'q4',
                        ('q2','c'):'q3',
                        ('q2','g'):'q6',
                        ('q3','b'):'q4',
                        ('q3','c'):'q7',
                        ('q3','g'):'q6',
                        ('q4','d'):'q5',
                        ('q4','e'):'q6',
                        ('q4','g'):'q6',
                        ('q5','f'):'q6',
                        ('q5','g'):'q6',}
    setAFData()
    # Creacion del automta
    automata = AF.AFD(alfabeto,estados,estados_aceptacion,estado_inicial,transiciones,traducir_alfabeto,desc_estado)
    #Leer cadenas del archivo cadenas.txt
    cadenas = readCadenas("cadenas.txt")
    #Validar cadenas
    print("==== Validando Cadenas ====")
    for cadena in cadenas:
        print(f"{automata.validarCadena(cadena)} : {cadena}")
def AFNDCaso2():
# Caso 2
    def setAFData():
            global alfabeto
            global traducir_alfabeto
            global estados
            global desc_estado
            global estado_inicial
            global estados_aceptacion
            global transiciones
            alfabeto = ('a','b','c','d','e','f','g')
            traducir_alfabeto = {"a": "tarjeta",
                                "b": "pinOK",
                                "c": "pinMal",
                                "d": "retirar",
                                "e": "saldo",
                                "f": "confirmar",
                                "g": "cancelar"}
    
            estados = ('q0','q1')
            desc_estado = {'q0':'Esperando tarjeta',
                        'q1':'Esperando PIN (1er intento)',
                        'q2':'Esperando PIN (2do intento)',
                        'q3':'Esperando PIN (3er intento)',
                        'q4':'Escoger operacion',
                        'q5':'Retiro',
                        'q6':'Operacion completada|Entregar recibo|Entregar dinero|Devilver tarjeta',
                        'q7':'Tarjeta bloqueada/retenida',}
            
            estado_inicial = 'q0'
            estados_aceptacion = ('q7','q6')
            transiciones = {('q0','a'):'q1',
                            ('q0','b'):'q0',
                            ('q0','c'):'q0',
                            ('q0','d'):'q0',
                            ('q0','e'):'q0',
                            ('q0','f'):'q0',
                            ('q0','g'):'q0',
                            ('q1','b'):'q4',
                            ('q1','c'):'q2',
                            ('q2','c'):'q3',
                            ('q3','c'):'q7',}
    setAFData()

    automata = AF.AFND(alfabeto,estados,estados_aceptacion,estado_inicial,transiciones,traducir_alfabeto,desc_estado)

    cadenas = ['accc']

    print("==== Validando Cadenas ====")
    for cadena in cadenas:
        print(f"{automata.validarCadena(cadena)} : {cadena}")
def printMenu():
    print('=== Aplicaciones AF ===')
    print('[1] Caso 1 - AFD')
    print('[2] Caso 2 - AFD')
    print('[3] Salir')
def automatonCases(opt_menu):
    while True:
        match (opt_menu):
            case 1:
                AFDCaso1()
                empty = input('Presione Enter/Intro para continuar...')
                opt_menu = 0
                break
            case 2:
                AFNDCaso2()
                opt_menu = 0
                break
            case 3:
                break

def ejecutar():
    cls()
    global opt_menu
    opt_menu = 0
    # Empieza el programa aqui
    while True:
        cls()
        printMenu()
        try:
            opt_menu = int(input('Seleccione una opcion: '))
            if (opt_menu in [1,2]):
                cls()
                automatonCases(opt_menu)
            elif(opt_menu == 3):
                break
            else:
                cls()
                print('-'*30)
                print("==>Escriba una opcion valida<==")
                print('-'*30)
        except ValueError:
            cls()
            print('-'*30)
            print("==>Escriba una opcion valida<==")
            print('-'*30)

# Ejecutar programa automata
ejecutar()