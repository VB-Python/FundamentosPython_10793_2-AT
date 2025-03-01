
'''Leitura e Escrita com chunking 
O método `chunking` permite ler ficheiros grandes sem sobrecarregar a RAM (ler e 
escrever em partes – chuncks). '''

with open("grande_ficheiro.txt", "r") as ficheiro: 
while chunk := ficheiro.read(1024):#Lê 1024 bytes de cada vez 
print(chunk) 