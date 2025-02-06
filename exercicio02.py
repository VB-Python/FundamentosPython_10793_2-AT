'''Escreva um programa que solicite ao utilizador dois números inteiros a
operação matemática a ser realizada (+,-,* e /).
Utilize a estrutura match...case para executar a operação escolhida e devolver
o resultado.'''


operacao    = str(input("especifique a operação desejada (+,-,*,/):"))
numero1     = int(input("Insira um primeiro valor:"))
numero2     = int(input("Insira um segundo valor:"))
conta       = float


match operacao:
    case "+":
        print("Resultado da operação é:" ,numero1 + numero2,)
    case "-":
        print("Resultado da operação é:" ,numero1 - numero2,)
    case "*":
        print("Resultado da operação é:" ,numero1 * numero2,)
    case "/":
            if numero2 == 0:
                print("Não é possivel dividir por zero")
            else:
                print("Resultado da operação = " ,numero1 / numero2,)
    case _:
        print("Operação inválida")



num1=int(input("Digita o primeiro número:\n---->\t"))
num2=int(input("Digita o segundo número:\n---->\t"))
operacao = input("Seleciona a operação a realizar (+, -, *, /):\n---->\t")
match operacao:
    case "+":
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        if num2 == 0:
            resultado = "Divisão por zero não é permitida"
        else:
            resultado = num1 / num2
    case _:
        resultado = "Operação inválida"
print("Resultado:", resultado)
#com duas // apresenta a divisão inteira
