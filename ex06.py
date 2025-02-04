''' Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e
converta o resultado para segundos, devolvendo o output para o ecrã (deverá ser
criado o ficheiro ex06.py).'''

import math

horas = input("Introduza o numero de horas:")
horas = int(horas)

minutos = input("Introduza o numero de minutos:")
minutos = int(minutos)

segundos = input("Introduza o numero de segundos:")
segundos = int(segundos)

print(f"o total em segundos é:{(horas*60*60)+(minutos*60)+segundos}")

