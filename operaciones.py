def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise ValueError("Ambos parámetros deben ser int o float")

def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        resultado = 0
        for _ in range(abs(int(b))):
            resultado += a
        if b < 0:
            resultado = -resultado
        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser int o float")
    
def dividir(dividendo, divisor):
    # Verificar que los valores sean int o float
    if not (isinstance(dividendo, (int, float)) and isinstance(divisor, (int, float))):
        return "Ambos valores deben ser de tipo int o float"
    
    # Verificar que el divisor no sea cero
    if divisor == 0:
        return "El divisor no puede ser cero"

    
    # Convertir los valores a números enteros para las iteraciones (si son flotantes)
    dividendo = abs(dividendo)
    divisor = abs(divisor)
    
    # Variable para contar cuántas veces se puede restar el divisor del dividendo
    cociente = 0
    
    # Realizar la división mediante restas sucesivas
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    
    # Devolver el resultado de la división
    return cociente

def factorial_recursivo(n):
    if not isinstance(n, int):
        raise ValueError("El valor debe ser un entero")
    if n < 0:
        raise ValueError("El valor debe ser un entero no negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    # Comprobamos que el valor sea un entero
    if not isinstance(n, int):
        raise ValueError("El valor debe ser un número entero.")
    
    # Comprobamos que el número sea no negativo
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a 0.")
    
    # Caso base para el factorial de 0 o 1
    if n == 0 or n == 1:
        return 1
    
    # Cálculo del factorial de manera iterativa
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    
    return resultado

def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("El parámetro debe ser un entero")
    if n < 0:
        raise ValueError("El parámetro debe ser un entero no negativo")
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
