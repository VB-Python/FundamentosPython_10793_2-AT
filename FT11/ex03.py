'''Escreve uma função em Python que dada uma lista de números imprime a soma
 dos valores dessa lista, o número de elementos da lista e a media desses 
valores.'''

import minhasfunc
dados = input("Escreve uma quantidade de números, divididos por espaço: ")
soma, conta_numeros, media = minhasfunc.numeros(dados)
print(f"A soma de todos os números é {soma}; a lista tem {conta_numeros} números e a média é {media}")


print("outra solução")


import minhasfunc

valores = [8,9,10]

res = minhasfunc.dadoslista(valores)
print("Sum: ", res[0])
print("Number of items: ", res[1])
print("Average: ", res[2])


