'''Escreve uma função em Python que dada uma palavra retorne o número de
 vogais nessa palavra. '''
 
 def conta_vogais(palavra):
    vogais = 'aeiou'
    count = 0
    for letra in palavra.lower():
        if letra in vogais:
            count += 1
    return count
print(conta_vogais('palavra')) # 3
print(conta_vogais('cão')) # 2

