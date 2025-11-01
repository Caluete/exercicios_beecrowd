# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
# caso haja uma divisão por 0 ou raiz de numero negativo.

"""Entrada
# Leia três valores de ponto flutuante (double) A, B e C."""

a, b, c = map(float, input().split())

delta = (b ** 2) - (4 * a * c)
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    R1 = (-b + delta ** 0.5) / (2 * a)
    R2 = (-b - delta ** 0.5) / (2 * a)
    print("R1 =", format(R1,'.5f'))
    print("R2 =", format(R2,'.5f'))