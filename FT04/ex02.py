'''Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de
uma pessoa.'''


print("Estado Civil: \n S. Solteiro/a;\n C. Casado/a;\n D. Divorciado/a;\n V. Viúvo/a.")



Estadocivil = str(input("Introduza o seu Estado Civil: "))


match Estadocivil:
    case "S":
        print("Solteiro/a")
    case "C":
        print("Casado/a")
    case "D":
        print("Divorciado/a")
    case "V":
        print("Viúvo/a")
    case _:
        print("Opção Inválida")
        