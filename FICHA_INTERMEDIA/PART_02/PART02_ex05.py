'''Reproduz o seguinte código que tem em conta o enunciado a seguir 
apresentado       : 
A empresa DataSecure precisa de um sistema que copie ficheiros binários de forma 
eficiente e segura. Para garantir a integridade dos dados, o sistema deve: 
a) Solicitar o nome de um ficheiro binário (ex.: imagem, PDF, áudio) que o 
utilizador deseja copiar. 
b) Criar uma cópia exata desse ficheiro, preservando os dados originais. 
c) Verificar se a cópia foi bem-sucedida, comparando os conteúdos dos dois 
ficheiros através do cálculo de um hash MD5. 
d) Exibir uma mensagem de sucesso ou erro informando se os ficheiros são 
idênticos. '''


import FICHA_INTERMEDIA.PART_02.DataSecure as DataSecure


#alinea a)
# Solicitar entrada do utilizador 
ficheiro_origem = input("Digite o nome do ficheiro binário a copiar: ")
#introduzi "grande_ficheiro.txt"
#alinea b)
ficheiro_destino = "copia_" + ficheiro_origem  # Criar nome para o ficheiro copiado 
# Executar a cópia e validação 
copiar_ficheiro_binario(ficheiro_origem, ficheiro_destino) 
#constatei a criação de um novo ficheiro "copia_grande_ficheiro.txt"


#alinea c)



