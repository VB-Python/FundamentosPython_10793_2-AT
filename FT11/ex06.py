'''Escreve uma função que, dado o número do mês retorne o mesmo, por extenso.'''

import minhasfunc
 
try:
numero = input("Introduza o número do mês: ")
    if numero >=0 and numero <=12:
        x = minhasfunc.ex5(numero)
        print(x)
    else:
        print("Número inválido, introduza novamente: ")


#OUtra forma

import main_funcoes as mf # Importa o módulo main_funcoes.py
input_mes = int(input("Digite o número do mês: ")) # Solicita o número do mês ao usuário
res = mf.mes_extenso(input_mes) # Chama a função mes_extenso do módulo main_funcoes
print(f"O mês {input_mes} é {mf.mes_extenso(input_mes)}") # Imprime o mês por extenso