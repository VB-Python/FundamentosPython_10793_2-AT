'''1. Leia uma cadeia de caracteres no formato “DD/MM/AAAA” e copie o dia, mês e ano para 
três variáveis inteiras.'''

Dia = int
Mes = int
Ano = int

try:
    # Leitura da data no formato DD/MM/AAAA
    data = input("Digite a data (DD/MM/AAAA): ")

    # Separando o dia, mês e ano
    dia, mes, ano = map(int, data.split('/'))
    #Trato todos os meses com 31 dias
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia < 32:
             # Exibindo os valores
            Dia = dia
            Mes = mes
            Ano = ano
            print(f"Dia: {dia}")
            print(f"Mês: {mes}")
            print(f"Ano: {ano}")
        else:
            print(f"O mês {mes} não tem {dia} dias")
    #Trato todos os meses com 30 dias
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia < 31:
                # Exibindo os valores
                Dia = dia
                Mes = mes
                Ano = ano
                print(f"Dia: {dia}")
                print(f"Mês: {mes}")
                print(f"Ano: {ano}")
            else:
                print(f"O mês {mes} não tem {dia} dias")
    #Trato Fevereiro, se Bissexto 29 dias, caso contrario 28 dias
    elif mes == 2:
            if ano % 400 == 0 or (ano % 100 != 0 and ano % 4 == 0):
                #print("O ano" , ano, "é Bissexto")
                if dia < 30:
                    # Exibindo os valores
                    Dia = dia
                    Mes = mes
                    Ano = ano
                    print(f"Dia: {dia}")
                    print(f"Mês: {mes}")
                    print(f"Ano: {ano}")
                else:
                    print(f"Em {ano} o mês {mes} não tem {dia} dias")
            else:
                #print("O ano" , ano, "não é Bissexto")
                if dia < 29:
                    # Exibindo os valores
                    Dia = dia
                    Mes = mes
                    Ano = ano
                    print(f"Dia: {dia}")
                    print(f"Mês: {mes}")
                    print(f"Ano: {ano}")
                else:
                    print(f"Em {ano} o mês {mes} não tem {dia} dias")


except ValueError:
    print("Erro: O formato da data deve ser DD/MM/AAAA e números inteiros.")

