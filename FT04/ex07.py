'''Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N)
em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito
utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não
sabíamos a fórmula).'''

natural = int(input("Introduza o numero de numeros naturais que pretende somar:"))
numero = 1
soma = 0
while numero <= natural:
    soma = soma + numero
    print(numero)
    numero = numero + 1 
    
    

print (f"quantidade de numeros naturais: {natural}, tem como resultado {soma}")

    