# Main.py
# Grupo 3 - Integrantes:
# Juan Pérez (20211234)
# María López (20219876)
# Carlos Ruiz (20214321)
# Ana Torres (20217654)

from funcionespuede import *

def main():
    while True:
        print("""
        Menu
        1. Tablero de 4 x 4
        2. Tablero de 6 x 8
        3. Tablero de 10 x 10
        4. Fin
        """)

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            jugar(4, 4)
        elif opcion == "2":
            jugar(6, 8)
        elif opcion == "3":
            jugar(10, 10)
        elif opcion == "4":
            print("Gracias por jugar.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
