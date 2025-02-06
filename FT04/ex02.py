'''Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de
uma pessoa.'''


print("Estado Civil: /n S. Solteiro;\n C. Casado;\n D. Divorciado;\n V. Viúvo.")



Estadocivil = float(input("Introduza o seu Estado Civil: "))


match Estadocivil:
    case S:
        print("Solteiro/a")
    case C:
        print("Casado/a")
    case D:
        print("Divorciado/a")
    case V:
        print("Viúvo/a")
    case _:
        print("Opção Inválida")
        