def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    # Ejemplos de uso
    print(sumar(7, 3))
    print(restar(7, 3))
    print(multiplicar(7, 3))
    print(dividir(7, 3))
