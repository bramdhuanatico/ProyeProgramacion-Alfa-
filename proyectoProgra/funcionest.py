# Colores ANSI
ROJO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"

def menu(opciones_tablero):
    print('Menu')
    for x, y in opciones_tablero.items():
        if x == 4:
            print(f'{x}. Fin')
        else:
            print(f'{x}. Tablero de {y[0]} x {y[1]}')

def seleccionar_opcion(opciones_tablero):
    opcion = int(input("Ingrese una opcion: "))
    while opcion not in opciones_tablero:
        print('Opcion invalida')
        opcion = int(input("Vuelva a ingresar una opcion: "))
    return opcion


def crear_tablero(filas, columnas):
    alto = 2 * filas - 1
    ancho = 2 * columnas - 1
    tablero = [[" " for x in range(ancho)] for x in range(alto)]

    for i in range(alto):
        for j in range(ancho):
            if i % 2 == 0 and j % 2 == 0:
                tablero[i][j] = "+"
            elif i % 2 == 0:
                tablero[i][j] = " "
            elif j % 2 == 0:
                tablero[i][j] = " "

    lista = [' '] * (columnas * 2 - 1)
    for i in range(len(lista)):
        if i % 2 == 0:
            numero = i // 2 + 1
            if numero == 1:
                lista[i] = ' ' + str(numero)
            else:
                lista[i] = str(numero)

    tablero.insert(0, lista)

    for i in range(len(tablero)):
        if i == 0:
            tablero[i].insert(0, ' ')
        elif i % 2 != 0:
            numero = (i + 1) // 2
            if numero <= 9:
                tablero[i].insert(0, ' ' + str(numero))
            else:
                tablero[i].insert(0, str(numero))
        else:
            tablero[i].insert(0, '  ')

    return tablero

def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()

def esta_en_rango(r, c, filas, columnas):
    return 1 <= r <= filas and 1 <= c <= columnas


def es_vecina_valida(origen, destino):
    if destino == origen:
        print("No pueden ser la misma coordenada.")
        return False
    dr = abs(destino[0] - origen[0])
    dc = abs(destino[1] - origen[1])
    if dr == 1 and dc == 0:
        return True
    elif dr == 0 and dc == 1:
        return True
    elif dr == 1 and dc == 1:
        print("No se permiten movimientos en diagonal.")
    else:
        print("Coordenada no está cerca del origen.")
    return False

def leer_coordenada(prompt, filas, columnas, origen=None):
    entrada = input(prompt)
    partes = entrada.strip().split()

    if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
        r, c = int(partes[0]), int(partes[1])
        if not esta_en_rango(r, c, filas, columnas):
            print("Coordenadas fuera de rango.")
            return leer_coordenada(prompt, filas, columnas, origen)
        if origen and not es_vecina_valida(origen, (r, c)):
            return leer_coordenada(prompt, filas, columnas, origen)
        return [r, c]
    else:
        print("Debe ingresar dos números válidos separados por espacio.")
        return leer_coordenada(prompt, filas, columnas, origen)

def colocar_linea(tablero, origen, destino, jugador):
    color = ROJO if jugador == 'A' else AZUL
    r1, c1 = origen[0] * 2 - 1, origen[1] * 2 - 1
    r2, c2 = destino[0] * 2 - 1, destino[1] * 2 - 1
    if r1 == r2:
        mid_c = (c1 + c2) // 2
        if tablero[r1][mid_c] == " ":
            tablero[r1][mid_c] = color + "-" + RESET
            verificar_cuadro(tablero, origen, destino, jugador)
            return True
        else:
            print("Esa línea ya está ocupada.")
    elif c1 == c2:
        mid_r = (r1 + r2) // 2
        if tablero[mid_r][c1] == " ":
            tablero[mid_r][c1] = color + "|" + RESET
            verificar_cuadro(tablero, origen, destino, jugador)
            return True
        else:
            print("Esa línea ya está ocupada.")
    return False


def contar_movimientos(filas, columnas):
    return (filas * (columnas - 1)) + ((filas - 1) * columnas)

def verificar_cuadro(tablero, origen, destino, jugador):
    color = ROJO if jugador == 'A' else AZUL
    r1, c1 = origen[0] * 2 - 1, origen[1] * 2 - 1
    r2, c2 = destino[0] * 2 - 1, destino[1] * 2 - 1
    cuadros_completados = 0

    if r1 == r2:
        cuadros_completados += verificar_cuadro_horizontal(tablero, r1, c1, c2, jugador, color)
    elif c1 == c2:
        cuadros_completados += verificar_cuadro_vertical(tablero, c1, r1, r2, jugador, color)

    return cuadros_completados > 0

def verificar_cuadro_horizontal(tablero, r1, c1, c2, jugador, color):
    completados = 0
    mid_col = (c1 + c2) // 2

    # Superior
    if r1 > 1 and tablero[r1][mid_col] == color + "-" + RESET:
        if tablero[r1-1][c1] != " " and tablero[r1-1][c2] != " " and tablero[r1-2][mid_col] != " ":
            if tablero[r1-1][mid_col] == " ":
                tablero[r1-1][mid_col] = color + jugador + RESET
                completados += 1

    # Inferior
    if r1 < len(tablero) - 2 and tablero[r1][mid_col] == color + "-" + RESET:
        if tablero[r1+1][c1] != " " and tablero[r1+1][c2] != " " and tablero[r1+2][mid_col] != " ":
            if tablero[r1+1][mid_col] == " ":
                tablero[r1+1][mid_col] = color + jugador + RESET
                completados += 1

    return completados

def verificar_cuadro_vertical(tablero, c1, r1, r2, jugador, color):
    completados = 0
    mid_row = (r1 + r2) // 2

    # Izquierda
    if c1 > 1 and tablero[mid_row][c1] == color + "|" + RESET:
        if tablero[r1][c1-1] != " " and tablero[r2][c1-1] != " " and tablero[mid_row][c1-2] != " ":
            if tablero[mid_row][c1-1] == " ":
                tablero[mid_row][c1-1] = color + jugador + RESET
                completados += 1

    # Derecha
    if c1 < len(tablero[0]) - 2 and tablero[mid_row][c1] == color + "|" + RESET:
        if tablero[r1][c1+1] != " " and tablero[r2][c1+1] != " " and tablero[mid_row][c1+2] != " ":
            if tablero[mid_row][c1+1] == " ":
                tablero[mid_row][c1+1] = color + jugador + RESET
                completados += 1

    return completados

def contar_puntaje(tablero):
    puntos_A = 0
    puntos_B = 0
    for fila in tablero:
        for celda in fila:
            if "A" in celda:
                puntos_A += 1
            elif "B" in celda:
                puntos_B += 1
    return puntos_A, puntos_B


def juegoIniciado(opcionesTablero, opcion):
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

        movimiento_valido = False
        while not movimiento_valido:
            origen = leer_coordenada("Ingrese origen (fila columna): ", filas, columnas)
            destino = leer_coordenada("Ingrese destino (fila columna): ", filas, columnas, origen)
            movimiento_valido = colocar_linea(tablero, origen, destino, jugador)

        jugador = 'B' if jugador == 'A' else 'A'

    imprimir_tablero(tablero)
    print("Tablero Lleno, juego terminado.")
    puntos_A, puntos_B = contar_puntaje(tablero)
    print(f"Puntaje final - A: {puntos_A} | B: {puntos_B}")

    if puntos_A > puntos_B:
        print("¡Jugador A gana el juego!")
    elif puntos_B > puntos_A:
        print("¡Jugador B gana el juego!")
    else:
        print("¡Empate!")