def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    else:
        return a / b

if __name__ == "__main__":
    print("5 + 3 =", sumar(5, 3))
    print("5 - 3 =", restar(5, 3))
    print("5 * 3 =", multiplicar(5, 3))
    print("5 / 3 =", dividir(5, 3))
    print("5 / 0 =", dividir(5, 0)) 
