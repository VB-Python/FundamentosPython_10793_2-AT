'''Escreve um programa que solicite um número inteiro ao utilizador e caso o mesmo seja
maior que 20, devolva o resultado da sua divisão por 2.'''

numero = int(input("Introduza um numero inteiro:"))


if numero > 20:
    print(f"Resultado da divisão por 2 é:{(numero/2)}")
else:
    print("Numero igual ou inferior a 20")
    