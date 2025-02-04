''' Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e
converta o resultado para segundos, devolvendo o output para o ecrã (deverá ser
criado o ficheiro ex06.py).'''

import math

horas = input("Introduza o numero de horas:")
horas = float(horas)

minutos = input("Introduza o numero de minutos:")
minutos = float(minutos)

segundos = input("Introduza o numero de segundos:")
segundos = float(segundos)

print(f"o total em segundos é:{(horas*60*60)+(minutos*60)+segundos}")

