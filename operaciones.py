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