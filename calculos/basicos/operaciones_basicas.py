def sumar(op1, op2):
    return op1 + op2

def restar(op1, op2):
    return op1 - op2

def multiplicar(op1, op2):
    return op1*op2

def dividir(op1, op2):
    if op2 != 0:
        return op1/op2
    else:
        return "No se puede dividir entre cero"