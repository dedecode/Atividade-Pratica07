import json
import os

def operar_json():
    nome_arquivo = 'pessoa.json'
    
    # --- Escrever dados no JSON ---
    print("--- Escrevendo dados no arquivo JSON ---")
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    cidade = input("Digite a cidade da pessoa: ")
    
    dados_pessoa = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade
    }

    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_pessoa, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo JSON: {e}")

    # --- Ler dados do JSON ---
    print("\n--- Lendo dados do arquivo JSON ---")
    if os.path.exists(nome_arquivo):
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                dados_lidos = json.load(f)
            
            print(f"Nome: {dados_lidos.get('nome', 'N/A')}")
            print(f"Idade: {dados_lidos.get('idade', 'N/A')}")
            print(f"Cidade: {dados_lidos.get('cidade', 'N/A')}")
        except FileNotFoundError: # Embora já verificado com os.path.exists, é boa prática
            print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        except json.JSONDecodeError:
            print(f"Erro: O arquivo '{nome_arquivo}' não é um JSON válido ou está vazio.")
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo JSON: {e}")
    else:
        print(f"O arquivo '{nome_arquivo}' ainda não existe para ser lido.")

operar_json()
