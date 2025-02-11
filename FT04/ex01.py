'''Faz um programa que escreva o nome do mês que é introduzido, pelo utilizador, na
forma numérica.'''


mes = int(input("Introduza o numero do mês: "))


match mes:
    case 1:
        print("JANEIRO")
    case 2:
        print("FEVEREIRO")
    case 3:
        print("MARÇO")
    case 4:
        print("ABRIL")
    case 5:
        print("MAIO")
    case 6:
        print("JUNHO")
    case 7:
        print("JULHO")
    case 8:
        print("AGOSTO")
    case 9:
        print("SETEMBRO")
    case 10:
        print("OUTUBRO")
    case 11:
        print("NOVEMBRO")
    case 12:
        print("DEZEMBRO")
    case _:
        print("VALOR INVÁLIDO")



"""Faz um programa que escreva o nome do mês que é introduzido, pelo utilizador, naforma numérica."""

# número do mês ao utilizador
numero_mes = int(input("Digite o número do mês (1 a 12): "))
match numero_mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Número de mês inválido!")