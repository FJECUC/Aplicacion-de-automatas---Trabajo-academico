from lib import AF
import os

def cls():
    '''Limpiar la consola'''
    os.system('cls')
def readCadenas(archivo:str):
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
        traducir_alfabeto = {
            "a": "tarjeta",
            "b": "pinOK",
            "c": "pinMal",
            "d": "retirar",
            "e": "saldo",
            "f": "confirmar",
            "g": "cancelar"}
        estados = ('q0','q1','q2','q3','q4','q5','q6')
        desc_estado = {
            'q0':'Esperando tarjeta',
            'q1':'Esperando PIN (1er intento)',
            'q2':'Esperando PIN (2do intento)',
            'q3':'Esperando PIN (3er intento)',
            'q4':'Escoger operacion',
            'q5':'Retiro',
            'q6':'Operacion completada|Entregar recibo|Entregar dinero|Devilver tarjeta',
            'q7':'Tarjeta bloqueada/retenida',}
        estado_inicial = 'q0'
        estados_aceptacion = ('q7','q6')
        transiciones = {
            ('q0','a'):'q1',
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
            ('q5','g'):'q6',
            }
    setAFData()
    # Creacion del automta
    automata = AF.AFD(alfabeto,estados,estados_aceptacion,estado_inicial,transiciones,traducir_alfabeto,desc_estado)
    #Leer cadenas del archivo cadenas.txt
    cadenas = readCadenas("AFDcadenas.txt")
    #Validar cadenas
    print("==== Validando Cadenas ====")
    for cadena in cadenas:
        trash = automata.validarCadena(cadena)
        #print(f"{automata.validarCadena(cadena)} : {cadena}")
#-------------------------------------------------------
def crearAutomataAFND():
    '''Crear AFND'''
    #Esta funcion es para tener las declaraciones en otra funcion
    alfabeto = ('r','b','i','g')
    traducir_alfabeto = {
        "r": "Reiniciar busqueda",
        "b": "Buscar disponibilidad",
        "i": "Seleccionar sala grupal",
        "g": "Seleccionar sala individual"}
    estados = ('q0','q1','q2','q3','q4')
    desc_estado = {
        'q0':'Esperando reinicio o busqueda',
        'q1':'Rama de busqueda de sala grupal',
        'q2':'Rama de busqueda de sala individual',
        'q3':'Reserva de sala grupal confirmada',
        'q4':'Reserva de sala individual confirmada'}
    estado_inicial = 'q0'
    estados_aceptacion = ('q7','q6')
    relaciones = {
        ('q0','r'):('q0'),
        ('q0','b'):('q1','q2'),
        ('q1','g'):('q3'),
        ('q2','i'):('q4')}
    return AF.AFND(alfabeto,estados,estados_aceptacion,estado_inicial,relaciones,traducir_alfabeto,desc_estado)
automataFND = crearAutomataAFND()
def AFNDCaso2(automata:AF.AFND):
# Caso 2
    automata_caso2 = automata
    cadenas = readCadenas('AFNDcadenas.txt')

    print("==== Validando Cadenas ====")
    for cadena in cadenas:
        trash=automata_caso2.validarCadena(cadena)
        #print(f"{automata.validarCadena(cadena)} : {cadena}")
# Aplicacion
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
                AFNDCaso2(automataFND)
                empty = input('Presione Enter/Intro para continuar...')
                opt_menu = 0
                break
            case 3:
                break

def ejecutar():
    cls()
    global opt_menu
    opt_menu = 0
    # Empieza el programa aqui
    cls()
    while True:
        printMenu()
        try:
            opt_menu = int(input('Seleccione una opcion: '))
            if (opt_menu in [1,2]):
                cls()
                automatonCases(opt_menu)
                cls()
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