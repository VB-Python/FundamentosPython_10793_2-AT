'''Sejam a e b os catetos de um triângulo retângulo, faz um programa que devolva o valor
da hipotenusa (deverá ser criado o ficheiro ex05.py).'''



print("Programa para calcular o valor da hipotenusa de um triangulo-rectangulo")

adjacente=input("Introduza o comprimento do cateto adjacente:")
adjacente=float(adjacente)

oposto=input("Introduza o comprimento do cateto oposto:")
oposto=float(oposto)

import math

hipotenusa= math.sqrt(adjacente**2 + oposto**2)

print(f"o comprimento da hipotenusa deste triangulo-rectangulo é:{hipotenusa}")