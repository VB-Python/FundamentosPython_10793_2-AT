''' Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos) e
converta o resultado para segundos, devolvendo o output para o ecrã (deverá ser
criado o ficheiro ex06.py).'''

horas = input("Introduza o numero de horas:")
horas = int(horas)

minutos = input("Introduza o numero de minutos:")
minutos = int(minutos)

segundos = input("Introduza o numero de segundos:")
segundos = int(segundos)

print(f"o total em segundos é:{(horas*60*60)+(minutos*60)+segundos}")

print("Vou lhe pedir para inserir uma quantidade de horas\n aquantidade de minutos e segundos\n e vou lhe dizer quantos segundos são.\n")
horas = input("Digite a quantidade de horas: ")
minutos = input("Digite a quantidade de minutos: ")
segundos = input("Digite a quantidade de segundos: ")
horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)
segundos = horas * 3600 + minutos * 60 + segundos
output = f"O total de segundos é: {segundos}"
print(output)