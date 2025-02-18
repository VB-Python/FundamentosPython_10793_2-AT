'''Considera a lista:
cores=["amarelo", "azul", "branco", "preto", "verde"]
Cria um programa, em python, que:
a. Faz o print de toda a lista
b. Faz o print do indíce 2 da lista
c. Altera o indíce 0 da lista para "vermelho"
d. Faz o print de toda a lista
e. Acrescenta no final da lista a cor "amarelo"
f. Faz o print de toda a lista
g. Acrescenta no indíce 2 a cor "roxo"
h. Faz o print de toda a lista
i. Apaga o último elemento da lista
j. Faz o print de toda a lista
k. Faz o print do tamanho da lista (len)'''


cores = ["amarelo", "azul", "branco", "preto", "verde"]

while True:
    print("\na - Faz o print de toda a lista")
    print("b - Faz o print do indíce 2 da lista")
    print("c - Altera o indíce 0 da lista para vermelho")
    print("d - Faz o print de toda a lista")
    print("e - Acrescenta no final da lista a cor amarelo")
    print("f - Faz o print de toda a lista")
    print("g - Acrescenta no indíce 2 a cor roxo")
    print("h - Faz o print de toda a lista")
    print("i - Apaga o último elemento da lista")
    print("j - Faz o print de toda a lista")
    print("k - Faz o print do tamanho da lista (len)")
    print("s - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "a":
            print (cores)

        case "b":
            print(cores[1])

        case "c":
            cores[0]="vermelho"

        case "d":
            print(cores)

        case "e":
            cores.append("amarelo")

        case "f":
            print(cores)

        case "g":
            cores[1]="roxo"

        case "h":
            print(cores)

        case "i":
            cores.pop()

        case "j":
            print(cores)

        case "k":
            print(len(lista))
            

        case "s":
            print("A sair do programa...")
            break

        case _:
            print("Opção inválida, tente novamente.")