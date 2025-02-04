'''Escreve um programa que receba dois números reais e indique qual o maior dos dois
números. Considera a possibilidade de o utilizador indicar dois números iguais.'''

nreal1 = float(input("Introduza um numero real:"))
nreal2 = float(input("Introduza um outro numero real:"))


if nreal1 > nreal2:
    print("O numero" ,nreal1, "é maior que o numero", nreal2,)
elif nreal1 < nreal2:
    print("O numero" ,nreal2, "é maior que o numero", nreal1,)
else:
    print("Indicou 2 numeros iguais:" ,nreal1,)


