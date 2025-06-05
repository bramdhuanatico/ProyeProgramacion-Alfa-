# Funciones para colores ANSI (no usan librerías)
RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

def crear_tablero(filas, columnas):
    alto = 2 * filas - 1
    ancho = 2 * columnas - 1
    tablero = [[" " for _ in range(ancho)] for _ in range(alto)]

    # Cruces y espacios
    for i in range(alto):
        for j in range(ancho):
            if i % 2 == 0 and j % 2 == 0:
                tablero[i][j] = "+"
            else:
                tablero[i][j] = " "

    # Numeración horizontal
    lista = [' '] * (ancho)
    for i in range(len(lista)):
        if i % 2 == 0:
            lista[i] = str(i // 2 + 1)
        else:
            lista[i] = ' '
    tablero.insert(0, lista)

    # Numeración vertical
    for i in range(len(tablero)):
        if i == 0:
            tablero[i].insert(0, ' ')
        elif i % 2 == 0:
            tablero[i].insert(0, ' ')
        else:
            tablero[i].insert(0, str(i // 2))
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        linea = ""
        for celda in fila:
            # Detecta si es línea y aplica color
            if celda == "-":
                linea += RED + celda + RESET + " "
            elif celda == "|":
                linea += BLUE + celda + RESET + " "
            elif celda == "A":
                linea += RED + celda + RESET + " "
            elif celda == "B":
                linea += BLUE + celda + RESET + " "
            else:
                linea += celda + " "
        print(linea)

def esta_en_rango(r, c, filas, columnas):
    return 1 <= r <= filas and 1 <= c <= columnas

def es_vecina_valida(origen, destino):
    if destino == origen:
        print("No pueden ser la misma coordenada.")
        return False
    dr = abs(destino[0] - origen[0])
    dc = abs(destino[1] - origen[1])
    if (dr == 1 and dc == 0) or (dr == 0 and dc == 1):
        return True
    if dr == 1 and dc == 1:
        print("No se permiten coordenadas en diagonal con respecto al origen.")
    else:
        print("Coordenada no está cerca del origen.")
    return False

def leer_coordenada(prompt, filas, columnas, origen=None):
    while True:
        entrada = input(prompt)
        partes = entrada.strip().split()
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            r, c = int(partes[0]), int(partes[1])
            if not esta_en_rango(r, c, filas, columnas):
                print("Coordenadas fuera de rango.")
                continue
            if origen and not es_vecina_valida(origen, (r,c)):
                continue
            return [r,c]
        else:
            print("Debe ingresar dos números válidos separados por espacio.")

def revisar_cuadrados(tablero, filas, columnas, jugador):
    cuadrados_completados = 0
    letra = jugador
    for fila in range(1, filas*2 - 1, 2):
        for col in range(1, columnas*2 - 1, 2):
            arriba = tablero[fila-1][col]
            abajo = tablero[fila+1][col]
            izquierda = tablero[fila][col-1]
            derecha = tablero[fila][col+1]
            centro = tablero[fila][col]

            if (arriba != " " and abajo != " " and izquierda != " " and derecha != " " and centro == " "):
                tablero[fila][col] = letra
                cuadrados_completados += 1
    return cuadrados_completados

def colocar_linea(tablero, origen, destino, jugador):
    # Convierte coordenadas de tablero (filas y columnas reales)
    filaOrigen = origen[0]*2 - 1
    colOrigen = origen[1]*2 - 1
    filaDestino = destino[0]*2 - 1
    colDestino = destino[1]*2 - 1

    if filaOrigen == filaDestino and abs(colOrigen - colDestino) == 2:
        # Línea horizontal
        colLinea = (colOrigen + colDestino)//2
        # Chequear si ya está ocupada
        if tablero[filaOrigen][colLinea] != " ":
            print("Esa línea ya está ocupada. Intenta otra.")
            return False
        # Color según jugador
        tablero[filaOrigen][colLinea] = "-" if jugador == "A" else "-"
    elif colOrigen == colDestino and abs(filaOrigen - filaDestino) == 2:
        # Línea vertical
        filaLinea = (filaOrigen + filaDestino)//2
        if tablero[filaLinea][colOrigen] != " ":
            print("Esa línea ya está ocupada. Intenta otra.")
            return False
        tablero[filaLinea][colOrigen] = "|" if jugador == "B" else "|"
    else:
        print("Coordenadas no están adyacentes correctamente.")
        return False
    return True

def jugar():
    filas, columnas = 4, 4
    tablero = crear_tablero(filas, columnas)
    max_movimientos = (filas * (columnas - 1)) + ((filas -1) * columnas)
    movimientos_realizados = 0
    jugador_actual = "A"

    while movimientos_realizados < max_movimientos:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}.")

        origen = leer_coordenada("Ingrese origen (fila columna): ", filas, columnas)
        destino = leer_coordenada("Ingrese destino (fila columna): ", filas, columnas, origen)

        if colocar_linea(tablero, origen, destino, jugador_actual):
            cuadrados = revisar_cuadrados(tablero, filas, columnas, jugador_actual)
            if cuadrados > 0:
                print(f"Jugador {jugador_actual} completó {cuadrados} cuadrado(s)!")
            else:
                # Cambiar jugador si no completó cuadrado
                jugador_actual = "B" if jugador_actual == "A" else "A"
            movimientos_realizados += 1
        else:
            print("Movimiento inválido, intente de nuevo.")

    imprimir_tablero(tablero)
    print("Juego terminado.")

if __name__ == "__main__":
    jugar()
