import sys

print("Operações:\n+ (soma)\n- (subtração)\nx (multiplicação)\n/ (divisão)\n^ (potência de)\nrz (raíz de)\nce (encerrar)\n-----------------")

x = int(input("Digite um número: "))
n = str(input("Qual a operação? "))

if n == "ce":
    sys.exit()

y = int(input("Digite um número: "))

if n == "+":
    r = x + y
elif n == "-":
    r = x - y
elif n == "x":
    r = x * y
elif n == "/":
    r = x / y
elif n == "^":
    r = x ** y
elif n == "rz":
    r = x ** (1/y)

print("Resultado:", r)

n = str(input("Qual a operação? "))

while n != "ce":
    z = int(input("Digite um número: "))

    if n == "+":
        r += z
    elif n == "-":
        r -= z
    elif n == "x":
        r *= z
    elif n == "/":
        r /= z
    elif n == "^":
        r = r ** z
    elif n == "rz":
        r = r ** (1/z)

    print("Resultado:", r)
    n = str(input("Qual a operação? "))