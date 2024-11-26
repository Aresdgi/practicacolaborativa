def mostrar_menu():
    while True:  # El ciclo continuará hasta que el usuario elija salir
        print("Seleccione una opción:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        # Solicitar opción al usuario
        opcion = input("Ingrese el número de la opción: ")

        # Verificar si la opción seleccionada es válida
        if opcion not in ['1', '2', '3', '4', '5']:
            print("Opción inválida. Intente de nuevo.")
            continue  # Si la opción es inválida, vuelve a mostrar el menú

        # Si la opción es 5, salir
        if opcion == '5':
            print("Saliendo del programa...")
            break

        # Si la opción no es salir, solicitar un número
        try:
            num = float(input("Ingrese un número: "))
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
            continue  # Si la entrada no es un número, vuelve a mostrar el menú