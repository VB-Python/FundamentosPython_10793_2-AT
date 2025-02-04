'''. Escreve um programa que solicite um número inteiro ao utilizador e verifique se o
mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato;
"O número [número] é [par/ímpar]"
Nota: um número é par quando o resto da divisão por 2 é zero.'''


numero = int(input("introduza um numero inteiro:"))


if numero % 2 == 0:
    print("O numero" ,numero, "é par")
else:
    print("O numero" ,numero, "é ímpar")


