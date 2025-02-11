'''Escreve um programa que coloque no ecrã a tabuada do número 5.'''


print("\nTabuada do número 5:")
numero = 5
tabuada = 5
multiplicacao = 5
for j in range(1,11):
    #print multiplicacao
    multiplicacao = numero * j
    print("%d*%d=%d\n" % (numero, j, multiplicacao)) #imprime o resultado
    
print("concluido")

