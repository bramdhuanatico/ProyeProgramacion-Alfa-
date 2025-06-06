from funcionest import *

opcionesTablero = {
    1: [4,4],
    2: [6,8],
    3: [10,10],
    4: 'Fin'
}


menu(opcionesTablero)
opcion = seleccionar_opcion(opcionesTablero)

if opcion in (1, 2, 3):
    juegoIniciado(opcionesTablero, opcion)
elif opcion == 4:
    print('Termina el programa')