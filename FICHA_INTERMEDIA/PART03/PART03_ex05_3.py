'''Cria um menu interativo para gerir a base de dados, onde o utilizador pode escolher entre:
1.- Adicionar um novo funcionário;
2.- Listar todos os funcionários;
3.- Atualizar o salário de um funcionário;
4.- Eliminar um funcionário;
5.- Sair.
Tenta implementar o seguinte código:'''


import sqlite3

try:
    
    def menu():
        while True:
            print("\nMENU DE GESTÃO DE FUNCIONÁRIOS")
            print("1. Adicionar funcionário")
            print("2. Listar funcionários")
            print("3. Atualizar salário")
            print("4. Eliminar funcionário")
            print("5. Salvar") #Acrescentei esta opção para atualizar na base de dados sem ter de sair.
            print("6. Sair")
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                nome = input("Nome: ")
                cargo = input("Cargo: ")
                salario = float(input("Salário: "))
                cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", (nome, cargo, salario))
            
            elif opcao == '2':
                cursor.execute("SELECT * FROM funcionarios")
                for funcionario in cursor.fetchall():
                    print(funcionario)
            
            elif opcao == '3':
                nome = input("Nome do funcionário: ")
                novo_salario = float(input("Novo salário: "))
                cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))
            
            elif opcao == '4':
                nome = input("Nome do funcionário a eliminar: ")
                cursor.execute("DELETE FROM funcionarios WHERE nome = ?", (nome,))
            
            elif opcao == '5':
                conn.commit()
            
            elif opcao == '6':
                conn.commit()
                conn.close()
                break
            else:
                print("Opção inválida! Tente novamente.")

    #Criar conexão
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()
    menu()

except FileNotFoundError: 
    print("Erro: O ficheiro não existe.") 
except Exception as e: 
    print(f"Ocorreu um erro inesperado: {e}") 