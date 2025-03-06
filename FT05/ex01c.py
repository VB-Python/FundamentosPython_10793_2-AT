'''Escreva um programa que gere 100 números reais aleatórios entre 0 e 1 e
armazene-os numa lista. No final o programa deverá mostrar as seguintes
informações:
i. Maior número;
ii. Menor número;
iii. Soma de todos os números gerados;
iv. Média e desvio padrão.'''


from random import random
from statistics import mean,stdev

lista=[]

for num in range(1,101):
    lista.append(random())

print(f'Maior número: {max(lista)}')
print(f'Menor número: {min(lista)}')
print(f'Soma dos números: {sum(lista)}')
print(f'Média dos números gerados: {mean(lista)}')
print(f'Desvio padrão dos números gerados: {stdev(lista)}')


print("outra solução")


import random
import statistics

numeros = [random.uniform(0, 1) for _ in range(100)]

print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("Soma de todos os números:", sum(numeros))
print("Média:", sum(numeros) / len(numeros))
print("Desvio padrão:", statistics.stdev(numeros))