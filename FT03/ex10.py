'''.Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador
deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores.
Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma
mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da
operação desejada.'''

operacao    = bool(input("especifique a operação desejada (+,-,*,/)"))
numero1     = int(input("Insira um primeiro valor"))
numero2     = int(input("Insira um segundo valor"))
conta       = float


if operacao == '+':
    print(numero1 + numero2)
elif operacao == '-':
    print(numero1 - numero2)
elif operacao == '*':
    print(numero1 * numero2)
elif operacao == '/':
    if numero2 == 0:
           print("Não é possivel dividir por zero")
    else:
    #print(numero1 / numero2)

    