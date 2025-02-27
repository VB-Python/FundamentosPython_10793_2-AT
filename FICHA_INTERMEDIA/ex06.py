'''Elabora uma script em python que peça ao utilizador dois números e devolva 
a divisão do primeiro número introduzido pelo seguinte. Trate erros como 
divisão por zero e valores inválidos. '''

try: 
    a = int(input("Digite o numerador: ")) 
    b = int(input("Digite o denominador: ")) 
    print("Resultado da divisão:", a / b) 
except ZeroDivisionError: 
    print("Erro: Não é possível dividir por zero.") 
except ValueError: 
    print("Erro: Apenas números inteiros são permitidos.") 


