from operaciones import sumar, restar, multiplicar, dividir, factorial_recursivo, factorial_iterativo, fibonacci

def mostrar_menu():
    while True:  # El ciclo continuará hasta que el usuario elija salir
        print("Seleccione una opción:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        print("6. Factorial iterativo")
        print("7. Calcular factorial de un numero recursivo")
        print("8. Calcular el fibonacci de un numero (iterativo)")

        # Solicitar opción al usuario
        opcion = input("Ingrese el número de la opción: ")

        # Verificar si la opción seleccionada es válida
        if opcion not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Opción inválida. Intente de nuevo.")
            continue  # Si la opción es inválida, vuelve a mostrar el menú

        # Si la opción es 5, salir
        if opcion == '5':
            print("Saliendo del programa...")
            break

        # Si la opción no es salir, solicitar los números necesarios
        try:
            if opcion in ['1', '2', '3', '4']:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            elif opcion in ['6', '7', '8']:
                num1 = int(input("Ingrese el número: "))
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
            elif opcion == '6':
                resultado = factorial_iterativo(num1)
            elif opcion == '7':
                resultado = factorial_recursivo(num1)
            elif opcion == '8':
                resultado = fibonacci(num1)
            else:
                print("Opción no implementada.")
                continue

            print(f"El resultado es: {resultado}")
        except ValueError as e:
            print(e)