from lib import AFD

def AFDcCaso1():
# Caso 1
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

    automata = AFD.AFD(alfabeto,estados,estados_aceptacion,estado_inicial,transiciones,traducir_alfabeto,desc_estado)

    cadenas = ['accc']

    print("==== Validando Cadenas ====")
    for cadena in cadenas:
        print(f"{automata.validarCadena(cadena)} : {cadena}")

def ejecutar():
    AFDcCaso1()

# Ejecutar programa automata
ejecutar()