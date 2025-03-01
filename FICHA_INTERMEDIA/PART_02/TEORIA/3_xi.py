
'''read() - Lê todo o ficheiro 
O método read( ) lê o conteúdo completo do ficheiro. Deve ser evitado para ficheiros 
muito grandes, pois pode sobrecarregar a RAM. '''

import exemplo.txt

with open("exemplo.txt", "r") as ficheiro: 
    conteudo = ficheiro.read() 
    print(conteudo) 