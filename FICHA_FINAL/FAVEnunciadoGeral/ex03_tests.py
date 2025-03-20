'''3. Escreve uma função em Python que dada uma lista de números imprime a soma dos 
valores dessa lista, o número de elementos da lista e a media desses valores. 
Implementa tratamento de exceções no teu código (try…except…else..finally). '''

import funcao

try:
    

    print("*** Programa para cálculo:\n Da soma, Do número, e Da média\n dos numeros introduzidos ***")
    
    dados = input("Escreve uma quantidade de números, separados por espaço: ")
    soma, conta_numeros, media = funcao.numeros(dados) #Solicita funcao.py
    
    print(f"A soma de todos os números é {soma}; a lista tem {conta_numeros} números e a média é {media}\n")
    print(f"Sum: ", soma)
    print(f"Number of items: ", conta_numeros)
    print(f"Average: ", media)
    

except ValueError:
    print("Erro: Por favor, insira apenas números válidos.")

finally:
        print("\nFim do processo.\n")