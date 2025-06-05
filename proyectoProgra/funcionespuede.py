# Funciones.py

def crear_tablero(filas, columnas):
    alto = 2 * filas + 1
    ancho = 2 * columnas + 1
    tablero = [[" " for _ in range(ancho)] for _ in range(alto)]

    for i in range(alto):
        for j in range(ancho):
            if i % 2 == 0 and j % 2 == 0:
                tablero[i][j] = "+"
            elif i % 2 == 0:
                tablero[i][j] = " "
            elif j % 2 == 0:
                tablero[i][j] = " "

    return tablero

def imprimir_tablero(tablero):
    print("   " + " ".join(str(i//2 + 1).rjust(2) for i in range(len(tablero[0])) if i % 2 == 0))
    for idx, fila in enumerate(tablero):
        if idx % 2 == 0:
            print("   " + "".join(fila))
        else:
            print(str(idx // 2 + 1).rjust(2) + " " + "".join(fila))

def movimiento_valido(tablero, origen, destino):
    r1, c1 = origen
    r2, c2 = destino
    r1, c1 = 2 * (r1 - 1), 2 * (c1 - 1)
    r2, c2 = 2 * (r2 - 1), 2 * (c2 - 1)

    if not (0 <= r1 < len(tablero) and 0 <= c1 < len(tablero[0]) and 0 <= r2 < len(tablero) and 0 <= c2 < len(tablero[0])):
        return False

    if abs(r1 - r2) + abs(c1 - c2) != 2:
        return False

    r, c = (r1 + r2) // 2, (c1 + c2) // 2
    return tablero[r][c] == " "

def trazar_linea(tablero, origen, destino, jugador):
    r1, c1 = origen
    r2, c2 = destino
    r1, c1 = 2 * (r1 - 1), 2 * (c1 - 1)
    r2, c2 = 2 * (r2 - 1), 2 * (c2 - 1)
    r, c = (r1 + r2) // 2, (c1 + c2) // 2
    tablero[r][c] = "-" if r1 == r2 else "|"
    return verificar_cuadros(tablero, r, c, jugador)

def verificar_cuadros(tablero, r, c, jugador):
    puntos = 0
    direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in direcciones:
        cr, cc = r + dr, c + dc
        if 0 < cr < len(tablero) - 1 and 0 < cc < len(tablero[0]) - 1:
            if (tablero[cr - 1][cc] != " " and tablero[cr + 1][cc] != " " and
                tablero[cr][cc - 1] != " " and tablero[cr][cc + 1] != " " and tablero[cr][cc] == " "):
                tablero[cr][cc] = jugador
                puntos += 1
    return puntos

def tablero_lleno(tablero):
    for i in range(1, len(tablero), 2):
        for j in range(1, len(tablero[0]), 2):
            if tablero[i][j] == " ":
                return False
    return True

def leer_coordenada(prompt, filas, columnas):
    while True:
        entrada = input(prompt)
        partes = entrada.strip().split()
        if len(partes) != 2:
            print("Debe ingresar dos números separados por espacio.")
            continue
        try:
            r, c = map(int, partes)
            if 1 <= r <= filas and 1 <= c <= columnas:
                return r, c
            else:
                print("Coordenadas fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingrese dos números.")

def jugar(filas, columnas):
    tablero = crear_tablero(filas, columnas)
    puntos = {"A": 0, "B": 0}
    turno = "A"

    while not tablero_lleno(tablero):
        imprimir_tablero(tablero)
        print(f"Turno del jugador {turno}. Puntajes - A: {puntos['A']}, B: {puntos['B']}")

        origen = leer_coordenada("Ingrese origen (fila columna): ", filas, columnas)
        destino = leer_coordenada("Ingrese destino (fila columna): ", filas, columnas)

        if not movimiento_valido(tablero, origen, destino):
            print("Movimiento inválido. Intente de nuevo.")
            continue

        obtenidos = trazar_linea(tablero, origen, destino, turno)
        puntos[turno] += obtenidos

        if obtenidos == 0:
            turno = "B" if turno == "A" else "A"

    imprimir_tablero(tablero)
    print(f"Juego terminado. Puntajes finales - A: {puntos['A']}, B: {puntos['B']}")
    if puntos['A'] > puntos['B']:
        print("Ganó el jugador A!")
    elif puntos['B'] > puntos['A']:
        print("Ganó el jugador B!")
    else:
        print("Empate!")
