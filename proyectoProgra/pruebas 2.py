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
            lista[i] = str(i // 2 + 1)
    tablero.insert(0, lista)

    for i in range(len(tablero)):
        if i == 0:
            tablero[i].insert(0, ' ')
        elif i % 2 != 0:
            numero = (i + 1) // 2
            if numero < 9:
                tablero[i].insert(0, ''+ str(numero))
            else:
                tablero[i].insert(0, str(numero))
        else:
            tablero[i].insert(0, ' ')

    return tablero


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
        print("No se permiten coordenadas en diagonal.")
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

            if origen:
                if not es_vecina_valida(origen, (r, c)):
                    continue

            return [r, c]
        else:
            print("Debe ingresar dos números válidos separados por espacio.")


def movimiento_ya_realizado(tablero, filaO, colO, filaD, colD):
    if filaO == filaD:
        f = filaO
        c = (colO + colD) // 2
    elif colO == colD:
        f = (filaO + filaD) // 2
        c = colO
    else:
        return True  # Diagonal no permitida, lo consideramos como hecho para bloquear
    return tablero[f][c] in ("|", "-")


def marcar_movimiento(tablero, filaO, colO, filaD, colD):
    if filaO == filaD:
        f = filaO
        c = (colO + colD) // 2
        tablero[f][c] = "-"
    elif colO == colD:
        f = (filaO + filaD) // 2
        c = colO
        tablero[f][c] = "|"


# ---------- INICIO DEL PROGRAMA ----------
filas, columnas = 4, 4
mat = crear_tablero(filas, columnas)

# Máximo de líneas posibles: horizontales + verticales
max_movimientos = (filas * (columnas - 1)) + ((filas - 1) * columnas)
movimientos_realizados = 0

while movimientos_realizados < max_movimientos:
    origen = leer_coordenada("Ingrese origen (fila, columna): ", filas, columnas)
    destino = leer_coordenada("Ingrese destino (fila, columna): ", filas, columnas, origen)

    filaO, colO = origen[0] * 2 - 1, origen[1] * 2 - 1
    filaD, colD = destino[0] * 2 - 1, destino[1] * 2 - 1

    if movimiento_ya_realizado(mat, filaO, colO, filaD, colD):
        print("Movimiento ya realizado. Intente con otra coordenada.\n")
        continue

    marcar_movimiento(mat, filaO, colO, filaD, colD)
    movimientos_realizados += 1

    print("\nEstado del tablero:")
    for fila in mat:
        print(" ".join(fila))
    print()

print("¡Tablero completo!")
