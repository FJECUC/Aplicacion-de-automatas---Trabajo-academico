from lib import AF

def AFDCaso1():
# Caso 1
    def setAFDData():
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
    setAFDData()

    automata = AF.AFD(alfabeto,estados,estados_aceptacion,estado_inicial,transiciones,traducir_alfabeto,desc_estado)

    cadenas = ['accc']

    print("==== Validando Cadenas ====")
    for cadena in cadenas:
        print(f"{automata.validarCadena(cadena)} : {cadena}")

def AFNDCaso2():

    automata = AF.AFND()

def ejecutar():
    global opt_menu
    opt_menu = 0

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
                    opt_menu = 0
                    break
                case 2:
                    AFNDCaso2()
                    opt_menu = 0
                    break
                case 3:
                    break

    printMenu()

    while True:
        opt_menu = int(input('Seleccione una opcion: '))
        if (opt_menu in [1,2]):
            automatonCases(opt_menu)
        elif(opt_menu == 3):
            break
        else:
            print('-'*30)
            printMenu()

# Ejecutar programa automata
ejecutar()