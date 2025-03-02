'''Leitura de um ficheiro CSV '''
import csv 
with open("dados.csv", newline='', encoding="utf-8") as ficheiro: 
    leitor = csv.reader(ficheiro) 
    for linha in leitor: 
        print(linha)m ficheiro CSV 
        
 ''' csv.reader() converte cada linha do ficheiro CSV numa lista de valores. 
  newline='' evita problemas com quebras de linha extras. 
  encoding="utf-8" garante compatibilidade com caracteres especiais. '''
  
  
'''     Ler um ficheiro CSV com cabeçalhos e converter para dicionário '''
import csv 
 
with open("dados.csv", newline='', encoding="utf-8") as ficheiro: 
    leitor = csv.DictReader(ficheiro)  # Converte cada linha num 
dicionário 
    for linha in leitor: 
        print(linha["Nome"], "-", linha["Idade"]) 
 
 ''' csv.DictReader( ) cria um dicionário onde as chaves são os nomes das colunas. 
  Facilita a extração de dados sem precisar de índices numéricos. '''
 
 
 '''    Escrita num ficheiro CSV – O código seguinte cria um ficheiro 
CSV com duas colunas (Nome, Idade). '''
import csv 
dados = [["Nome", "Idade"], ["João", 25], ["Ana", 30]] 
with open("dados.csv", "w", newline='', encoding="utf-8") as ficheiro: 
    escritor = csv.writer(ficheiro) 
    escritor.writerows(dados) 
 
'''  writerows() escreve múltiplas linhas de uma vez. 
  Se o ficheiro já existir, será sobrescrito. '''
 
 
 '''    Acrescentar dados a um ficheiro CSV existente '''
import csv 
 
novos_dados = [ 
    ["Carlos", 35, "Braga"], 
    ["Ana", 40, "Faro"] 
] 
 
with open("novo_arquivo.csv", "a", newline='', encoding="utf-8") as 
ficheiro: 
    escritor = csv.writer(ficheiro) 
    escritor.writerows(novos_dados)  # Adiciona novas linhas sem apagar 
as existentes 
 
'''  O modo "a" permite acrescentar conteúdo sem apagar os dados existentes. '''
 
 
 
'''     Escrever ficheiros CSV formatados com DictWriter '''
import csv 
dados = [ 
{"Nome": "João", "Idade": 25, "Cidade": "Lisboa"}, 
{"Nome": "Maria", "Idade": 30, "Cidade": "Porto"} 
] 
with open("dados_formatados.csv", "w", newline='', encoding="utf-8") as 
ficheiro: 
campos = ["Nome", "Idade", "Cidade"] 
escritor = csv.DictWriter(ficheiro, fieldnames=campos) 
escritor.writeheader()  # Escreve os cabeçalhos 
escritor.writerows(dados)  # Escreve os dados 

'''DictWriter() permite escrever ficheiros CSV diretamente a partir de dicionários. 
writeheader() escreve os cabeçalhos no ficheiro automaticamente.'''
