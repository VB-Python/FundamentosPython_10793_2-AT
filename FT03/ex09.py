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
peso    = float(input("Introduza o seu peso, em Kg:"))
altura  = float(input("Introduza a sua altura, metros:"))


imc = peso/(altura*altura)

print("Resultado e Classificação do seu IMC:")

if imc < 17:
    print(nome,"," , idade, "anos, ",peso, "Kg, e" ,altura, "metros de altura :" , imc, "IMC<17 - Muito abaixo do peso ideal")
elif 17 <= imc and imc < 18.5:
    print(nome,"," , idade, "anos, ",peso, "Kg, e" ,altura, "metros de altura :" , imc, "17<=IMC<18,5 - Abaixo do peso ideal")
elif 18.5 <= imc and imc < 25:
    print(nome,"," , idade, "anos, ",peso, "Kg, e" ,altura, "metros de altura :" , imc, "18,5<=IMC<25 - Peso normal")
elif 25 <= imc and imc < 30:
    print(nome,"," , idade, "anos, ",peso, "Kg, e" ,altura, "metros de altura :" , imc, "25<=IMC<30 - Acima do peso ideal")
elif 30 <= imc and imc < 35:
    print(nome,"," , idade, "anos, ",peso, "Kg, e" ,altura, "metros de altura :" , imc, "30<=IMC<35 - Obesidade I")
elif 35 <= imc and imc < 40:
    print(nome,"," , idade, "anos, ",peso, "Kg, e" ,altura, "metros de altura :" , imc, "35<=IMC<40 - Obesidade II (severa)")
elif imc >= 40:
    print(nome,"," , idade, "anos, ",peso, "Kg, e" ,altura, "metros de altura :" , imc, "IMC>=40 - Obesidade III (mórbida)")


nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
IMC = round(peso / (altura * altura), 2)
if IMC < 17:
    
    print(f"{nome} seu IMC é {IMC} você está muito abaixo do peso ideal!")
elif IMC >= 17 and IMC < 18.5:
    print(f"{nome} seu IMC é {IMC} você está abaixo do peso!")
    
elif IMC >= 18.5 and IMC < 25:
    print(f"{nome} seu IMC é {IMC} você está no peso normal!")
    
elif IMC >= 25 and IMC < 30:
    
    print(f"{nome} seu IMC é {IMC} você está acima do peso!")
    
elif IMC >= 30 and IMC < 35:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade I!")
elif IMC >= 35 and IMC < 40:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade II (severa)!")
    
else:
    
    print(f"{nome} seu IMC é {IMC} você está em obesidade III (mórbida)!")