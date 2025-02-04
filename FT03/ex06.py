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
else:
    print("O terceiro numero introduzido" ,nreal3, "é o maior dos 3 numeros")



