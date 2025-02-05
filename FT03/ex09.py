'''O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa.
Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que,
de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado de
acordo com as seguintes condições:
• IMC<17 - Muito abaixo do peso ideal
• 17<=IMC<18,5 - Abaixo do peso
• 18,5<=IMC<25 - Peso normal
• 25<=IMC<30 - Acima do peso
• 30<=IMC<35 - Obesidade I
• 35<=IMC<40 - Obesidade II (severa)
• IMC>=40 - Obesidade III (mórbida)
 Nota: IMC=massa/(altura*altura)
'''

nome    = str(input("Introduza o seu nome:"))
idade   = int(input("Introduza a sua idade:"))
peso    = float(input("Introduza o seu peso:"))
altura  = float(input("Introduza a sua altura:"))


imc = peso/(altura*altura)

print("Resultado e Classificação do seu IMC:")

if imc < 17:
    print("IMC<17 - Muito abaixo do peso ideal")
elif 17 <= imc and imc < 18.5:
    print("17<=IMC<18,5 - Abaixo do peso ideal")
elif 18.5 <= imc and imc < 25:
    print("18,5<=IMC<25 - Peso normal")
elif 25 <= imc and imc < 30:
    print("25<=IMC<30 - Acima do peso ideal")
elif 30 <= imc and imc < 35:
    print("30<=IMC<35 - Obesidade I")
elif 35 <= imc and imc < 40:
    print("35<=IMC<40 - Obesidade II (severa)")
elif imc >= 40:
    print("IMC>=40 - Obesidade III (mórbida)")


