compras = []
total_gastado = 0


def agregar_compra():
    global total_gastado

    monto = input("Ingrese el monto de la compra: ")
    try:
        monto = int(monto)
        compras.append(monto)
        total_gastado += monto
        print(f"Compra de {monto} ingresada correctamente.")
    except ValueError:
        print("Dato ingresado no parece numerico")


def mostrar_compras():
    for i, item in enumerate(compras):
        print(f"Compra {i} - {item}")

    if len(compras) == 0:
        print("No hay compras registradas")


def mostrar_total():
    print(f"Total gastado: ${total_gastado:.2f}")


def menu():
    while True:
        print("")
        print("Menu:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == '1':
            agregar_compra()
        elif opcion == '2':
            mostrar_compras()
        elif opcion == '3':
            mostrar_total()
        elif opcion == '4':
            exit()
        else:
            print("Opcion inválida")


def main():
    menu()


if __name__ == "__main__":
    main()
