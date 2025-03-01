'''write() - Escrever num ficheiro 
O método write( ) escreve diretamente num ficheiro e sobrescreve o seu conteúdo.'''
 
with open("exemplo.txt", "w") as ficheiro: 
    ficheiro.write("Esta é a nova primeira linha.") 
    ficheiro.write("Segunda linha do ficheiro.")