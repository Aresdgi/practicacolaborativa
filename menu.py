from operaciones import sumar, restar, multiplicar, dividir

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

        # Si la opción no es salir, solicitar dos números
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")
            continue

        # Realizar la operación seleccionada
        try:
            if opcion == '1':
                resultado = sumar(num1, num2)
            elif opcion == '2':
                resultado = restar(num1, num2)
            elif opcion == '3':
                resultado = multiplicar(num1, num2)
            elif opcion == '4':
                resultado = dividir(num1, num2)
            else:
                print("Opción no implementada.")
                continue

            print(f"El resultado es: {resultado}")
        except ValueError as e:
            print(e)