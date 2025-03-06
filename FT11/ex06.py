'''Escreve uma função que, dado o número do mês retorne o mesmo, por extenso.'''

import minhasfunc
 
try:
numero = input("Introduza o número do mês: ")
    if numero >=0 and numero <=12:
        x = minhasfunc.ex5(numero)
        print(x)
    else:
        print("Número inválido, introduza novamente: ")


