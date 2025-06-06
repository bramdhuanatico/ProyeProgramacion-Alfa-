from funciones import *

opcionesTablero = {
    1: [4,4],
    2: [6,8],
    3: [10,10],
    4: 'Fin'
}
print('Menu')
for x,y in opcionesTablero.items():
    if x == 4:
        print(f'{x}. Fin')
    else:
        print(f'{x}. Tablero de {y[0]} x {y[1]}')

opcion = int(input("Ingrese una opcion: "))
while opcion < 1 or opcion > 4:
    print('Opcion invalida')
    opcion = int(input("Vuelva a ingresar una opcion: "))

if opcion == 1:
    filas, columnas = opcionesTablero[opcion][0], opcionesTablero[opcion][1]
    tablero = crear_tablero(filas, columnas)
    max_movimientos = contar_movimientos(filas, columnas)
    jugador = 'A'
    for i in range(max_movimientos):
        puntos_A, puntos_B = contar_puntaje(tablero)
        print(f"Puntaje - A: {puntos_A} | B: {puntos_B}")
        imprimir_tablero(tablero)
        print()
        print(f"Turno del jugador {jugador}")
        while True:
            origen = leer_coordenada("Ingrese origen (fila columna): ", filas, columnas)
            destino = leer_coordenada("Ingrese destino (fila columna): ", filas, columnas, origen)
            if colocar_linea(tablero, origen, destino, jugador):
                break
        jugador = 'B' if jugador == 'A' else 'A'

    imprimir_tablero(tablero)
    print("Juego terminado.")
    puntos_A, puntos_B = contar_puntaje(tablero)
    print(f"Puntaje final - A: {puntos_A} | B: {puntos_B}")

    if puntos_A > puntos_B:
        print("¡Jugador A gana el juego!")
    elif puntos_B > puntos_A:
        print("¡Jugador B gana el juego!")
    else:
        print("¡Empate!")

elif opcion == 2:
    filas, columnas = opcionesTablero[opcion][0], opcionesTablero[opcion][1]
    tablero = crear_tablero(filas, columnas)
    max_movimientos = contar_movimientos(filas, columnas)
    jugador = 'A'
    for i in range(max_movimientos):
        puntos_A, puntos_B = contar_puntaje(tablero)
        print(f"Puntaje - A: {puntos_A} | B: {puntos_B}")
        imprimir_tablero(tablero)
        print()
        print(f"Turno del jugador {jugador}")
        while True:
            origen = leer_coordenada("Ingrese origen (fila columna): ", filas, columnas)
            destino = leer_coordenada("Ingrese destino (fila columna): ", filas, columnas, origen)
            if colocar_linea(tablero, origen, destino, jugador):
                break
        jugador = 'B' if jugador == 'A' else 'A'

    imprimir_tablero(tablero)
    print("Juego terminado.")
    puntos_A, puntos_B = contar_puntaje(tablero)
    print(f"Puntaje final - A: {puntos_A} | B: {puntos_B}")

    if puntos_A > puntos_B:
        print("¡Jugador A gana el juego!")
    elif puntos_B > puntos_A:
        print("¡Jugador B gana el juego!")
    else:
        print("¡Empate!")

elif opcion == 3:
    filas, columnas = opcionesTablero[opcion][0], opcionesTablero[opcion][1]
    tablero = crear_tablero(filas, columnas)
    max_movimientos = contar_movimientos(filas, columnas)
    jugador = 'A'
    for i in range(max_movimientos):
        puntos_A, puntos_B = contar_puntaje(tablero)
        print(f"Puntaje - A: {puntos_A} | B: {puntos_B}")
        imprimir_tablero(tablero)
        print()
        print(f"Turno del jugador {jugador}")
        while True:
            origen = leer_coordenada("Ingrese origen (fila columna): ", filas, columnas)
            destino = leer_coordenada("Ingrese destino (fila columna): ", filas, columnas, origen)
            if colocar_linea(tablero, origen, destino, jugador):
                break
        jugador = 'B' if jugador == 'A' else 'A'

    imprimir_tablero(tablero)
    print("Juego terminado.")
    puntos_A, puntos_B = contar_puntaje(tablero)
    print(f"Puntaje final - A: {puntos_A} | B: {puntos_B}")

    if puntos_A > puntos_B:
        print("¡Jugador A gana el juego!")
    elif puntos_B > puntos_A:
        print("¡Jugador B gana el juego!")
    else:
        print("¡Empate!")

elif opcion == 4:
    print('Termina el programa')