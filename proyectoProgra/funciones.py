# Colores ANSI
ROJO = "\033[91m"
AZUL = "\033[94m"
RESET = "\033[0m"


def crear_tablero(filas, columnas):
    alto = 2 * filas - 1
    ancho = 2 * columnas - 1
    tablero = [[" " for x in range(ancho)] for x in range(alto)]

    for i in range(alto):
        for j in range(ancho):
            if i % 2 == 0 and j % 2 == 0:
                tablero[i][j] = "+"

    lista = [' '] * (columnas * 2 - 1)
    for i in range(len(lista)):
        lista[i] = str(i // 2 + 1) if i % 2 == 0 else ' '
    tablero.insert(0, lista)

    for i in range(len(tablero)):
        numero = i + 1
        if i % 2 == 0:
            tablero[i].insert(0, ' ')
        else:
            tablero[i].insert(0, str(numero // 2))

    return tablero


def imprimir_tablero(tablero):
    for fila in tablero:
        for elem in fila:
            print(elem, end=" ")
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
    while True:
        entrada = input(prompt)
        partes = entrada.strip().split()
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            r, c = int(partes[0]), int(partes[1])
            if not esta_en_rango(r, c, filas, columnas):
                print("Coordenadas fuera de rango.")
                continue
            if origen and not es_vecina_valida(origen, (r, c)):
                continue
            return [r, c]
        else:
            print("Debe ingresar dos números válidos separados por espacio.")


def colocar_linea(tablero, origen, destino, jugador):
    color = ROJO if jugador == 'A' else AZUL
    r1, c1 = origen[0] * 2 - 1, origen[1] * 2 - 1
    r2, c2 = destino[0] * 2 - 1, destino[1] * 2 - 1
    if r1 == r2:
        mid_c = (c1 + c2) // 2
        if tablero[r1][mid_c] == " ":
            tablero[r1][mid_c] = color + "-" + RESET
            return True
        else:
            print("Esa línea ya está ocupada.")
    elif c1 == c2:
        mid_r = (r1 + r2) // 2
        if tablero[mid_r][c1] == " ":
            tablero[mid_r][c1] = color + "|" + RESET
            return True
        else:
            print("Esa línea ya está ocupada.")
    return False


def contar_movimientos(filas, columnas):
    return (filas * (columnas - 1)) + ((filas - 1) * columnas)