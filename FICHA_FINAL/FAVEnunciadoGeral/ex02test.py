'''2. Escreve uma função em Python que dada uma palavra retorne o número de vogais nessa 
palavra. '''

import funcao

palavra = input("Contagem de vogais - Escreva uma palavra: ")
vogais = funcao.conta_vogais(palavra):
print(count)


def conta_vogais(palavra):
    vogais = 'aeiou'
    count = 0
    for letra in palavra.lower():
        if letra in vogais:
            count += 1
    return count
print(conta_vogais('palavra')) # 3
print(conta_vogais('cão')) # 2

##########################################################

def info_str(palavra="AEc"):
    count_vogais=0
    for x in palavra:
        if x in ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]:
            count_vogais+=1
    
    return count_vogais

##########################################################


 
import minhasfunc
 
elemento = input("Escreva uma frase: ")
mês = minhasfunc.ex5(elemento)
print(mês)

##########################################################
def ex5(elemento):
    elementos = []
    for p in elemento:
        if p not in elementos:
            elementos.append(p)
    return elementos
##########################################################