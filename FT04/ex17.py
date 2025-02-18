'''Escreva um programa que peça ao utilizador 20 números reais 
e no final mostre a soma e a média dos números introduzidos'''


soma=0
for i in range(20):
    n = float(input("Introduza um número real: "))
    soma = soma + n

media = soma/20

print("Soma:",soma)
print("Media:",media)
