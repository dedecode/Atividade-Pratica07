import csv

def ler_dados_csv():
    nome_arquivo = 'pessoas.csv'
    
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            print(f"\nConteúdo do arquivo '{nome_arquivo}':")
            encontrou_dados = False
            for row in reader:
                encontrou_dados = True
                print(f"Nome: {row.get('Nome', 'N/A')}, Idade: {row.get('Idade', 'N/A')}, Cidade: {row.get('Cidade', 'N/A')}")
            
            if not encontrou_dados:
                print("O arquivo CSV está vazio ou não contém dados.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado. Certifique-se de que ele existe e está na mesma pasta.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo CSV: {e}")

ler_dados_csv()
