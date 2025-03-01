'''append() - Acrescentar conteúdo ao ficheiro 
O método append( ) adiciona conteúdo ao final do ficheiro sem sobrescrever o 
conteúdo existente. '''

with open("exemplo.txt", "a") as ficheiro: 
ficheiro.write("Nova linha adicionada.") 