'''. Reescreve o programa anterior de forma a apresentar a tabuada de qualquer número
introduzido pelo utilizador.
'''

tabuada = int(input("Introzuda o numero para a qual pretende obter a tabuada:"))

print("\nTabuada do número 5:")
numero1 = 0

multiplicacao = tabuada
while numero1 <= 10:
    
    multiplicacao = tabuada * numero1 
    print(f"{tabuada} x {numero1} = {multiplicacao}")
    numero1 = numero1 + 1