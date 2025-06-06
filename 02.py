import csv

def escrever_dados_csv():
    nome_arquivo = 'pessoas.csv'
    
    print("Vamos adicionar informações de pessoas ao arquivo CSV.")
    print("Digite 'sair' a qualquer momento para finalizar.")

    dados_para_escrever = []
    
    while True:
        nome = input("Nome (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        
        idade = input("Idade: ")
        cidade = input("Cidade: ")
        
        dados_para_escrever.append({'Nome': nome, 'Idade': idade, 'Cidade': cidade})
        print("Pessoa adicionada. Digite mais uma ou 'sair'.")

    try:
        # Abre o arquivo em modo de escrita ('w') com newline='' para evitar linhas em branco
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
            # Define as colunas (cabeçalho)
            fieldnames = ['Nome', 'Idade', 'Cidade']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader() # Escreve o cabeçalho
            writer.writerows(dados_para_escrever) # Escreve as linhas de dados

        print(f"\nDados salvos com sucesso em '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo CSV: {e}")

escrever_dados_csv()
