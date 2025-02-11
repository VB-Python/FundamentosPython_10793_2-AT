'''. Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número
introduzido pelo utilizador.
'''


tabuada = int(input("Introzuda o numero para a qual pretende obter a tabuada:"))


multiplicacao = tabuada
for j in range(1,11):
    #print multiplicacao
    multiplicacao = tabuada * j
    print("%d*%d=%d\n" % (tabuada, j, multiplicacao)) #imprime o resultado
    
print("concluido")

