from lib import AFD

# Ejemplo de AFD
alfabeto = ('0','1')
estados = ('q0','q1')
estado_inicial = 'q0'
estados_aceptacion = ('q1')
transiciones = {('q0','0'):'q0',
                ('q0','1'):'q1',
                ('q1','0'):'q0',
                ('q1','1'):'q1',}

automata = AFD.AFD(alfabeto,estados,estados_aceptacion,estado_inicial,transiciones)

cadenas = ['1','1110','0101','00110']

print("==== Validando Cadenas ====")
for cadena in cadenas:
    print(f"{automata.validarCadena(cadena)} : {cadena}")