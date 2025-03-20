'''3. Escreve uma função em Python que dada uma lista de números imprime a soma dos 
valores dessa lista, o número de elementos da lista e a media desses valores. 
Implementa tratamento de exceções no teu código (try…except…else..finally). '''

import funcao
print("*** Programa para cálculo:\n Da soma, Do número, e Da média\n dos numeros introduzidos ***")
dados = input("Escreve uma quantidade de números, separados por espaço: ")
soma, conta_numeros, media = funcao.numeros(dados)
print(f"A soma de todos os números é {soma}; a lista tem {conta_numeros} números e a média é {media}")
print("Sum: ", res[0])
print("Number of items: ", res[1])
print("Average: ", res[2])



'''Escreve uma função em Python que dada uma lista de números imprime a soma
 dos valores dessa lista, o número de elementos da lista e a media desses 
valores.'''

import minhasfunc
dados = input("Escreve uma quantidade de números, separados por espaço: ")
soma, conta_numeros, media = minhasfunc.numeros(dados)
print(f"A soma de todos os números é {soma}; a lista tem {conta_numeros} números e a média é {media}")
print("Sum: ", res[0])
print("Number of items: ", res[1])
print("Average: ", res[2])





##########################################################
def numeros(dados):
    import statistics
    user = list(map(int, dados.split()))
    soma = sum(user)
    conta_numeros = len(user)
    media = statistics.mean(user)
    return soma, conta_numeros, media
##########################################################
