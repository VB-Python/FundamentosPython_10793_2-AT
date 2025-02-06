'''Escreve um programa que receba três números reais e indique qual o maior dos três
números. '''

nreal1 = float(input("Introduza um primeiro numero real:"))
nreal2 = float(input("Introduza um segundo numero real:"))
nreal3 = float(input("Introduza um terceiro e ultimo numero real:"))


if nreal1 > nreal2:
    if nreal1 > nreal3:
        print("O primeiro numero introduzido" ,nreal1, "é o maior dos 3 numeros")
    elif nreal3 > nreal2:
        print("O terceiro numero introduzido" ,nreal3, "é o maior dos 3 numeros")
    
elif nreal2 > nreal1:
    if nreal2 > nreal3:
        print("O segundo numero introduzido" ,nreal2, "é o maior dos 3 numeros")
    elif nreal3 > nreal1:
        print("O terceiro numero introduzido" ,nreal3, "é o maior dos 3 numeros")
elif nreal1 == nreal2 == nreal3:
    print("Os numeros introduzidos foram iguais: " ,nreal3,)
else:
    print("O terceiro numero introduzido" ,nreal3, "é o maior dos 3 numeros")



# Solicita três números reais ao utilizador
numero1 = float(input("Por favor, insira o primeiro número real: "))
numero2 = float(input("Por favor, insira o segundo número real: "))
numero3 = float(input("Por favor, insira o terceiro número real: "))
#1 Encontra o maior número entre os três
maior = numero1   #maior é definido como numero1. ponto de partida para fazer a comparação.
#2 o código verifica se numero2 ou numero3 são maiores que o valor atual de maior. Se for o caso, maior é atualizado para o novo valor mais alto. 
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
# Imprime o maior número
print(f"O maior número é {maior}.")