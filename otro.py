def sumar (a, b):
    return a + b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre 0")
    return a / b

def restar (a, b):
    return a - b

num1 = float(input("Ingresa el primer número: "))
operacion = input("Ingresa la operación ( +, -, *, / ): ")
num2 = float(input("Ingresa el segundo número: "))

if operacion == "+":
    resultado = sumar(num1, num2)

elif operacion == "*":
    resultado = multiplicar(num1, num2)

elif operacion == "/":
    resultado = dividir(num1, num2)

elif operacion == "-":
    resultado = restar(num1, num2)

else:
    print("Operacion no valida o incorecta")

print(f"resultado: {resultado}")