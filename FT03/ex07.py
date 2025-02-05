''' Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser
um ano bissexto é: o ano deve ser divisível por 400; ou se for divisível por 4 e não for
divisível por 100.'''

ano = int(input("Introduza um ano a fim de averiguar se é Bissexto:"))

if ano % 400 == 0: # não funciona
    print("O ano" , ano, "é Bissexto")
else:
    print("O ano" , ano, "não é Bissexto")



ano = int(input("Introduza um ano a fim de averiguar se é Bissexto:"))

if ano % 4 == 0:
    if ano % 100 != 0:
        print("O ano" , ano, "é Bissexto")
else:
    print("O ano" , ano, "não é Bissexto")



ano = int(input("Introduza um ano a fim de averiguar se é Bissexto:"))
if ano % 400 == 0 or ano % 100 != 0 and ano % 4 ==0: # primeira condição não funciona
    print("O ano" , ano, "é Bissexto")
else:
    print("O ano" , ano, "não é Bissexto")


