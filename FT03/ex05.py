''' Escreva um programa que verifique se um determinado número introduzido pelo
utilizador é nulo, positivo ou negativo.'''

numero = float(input("Introduza um numero:"))



if numero == 0:
    print("O numero" ,numero, "é nulo")
elif numero > 0:
    print("O numero" ,numero, "é positivo")
elif numero < 0:
    print("O numero" ,numero, "é negativo")

"""Escreva um programa que verifique se um determinado número introduzido pelo
utilizador é nulo, positivo ou negativo."""

numero = float(input("Introduza um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é nulo.")