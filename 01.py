import re
import numpy as np

def analisar_logs():
    nome_arquivo = input("Digite o nome do arquivo de log (ex: log_treinamento.txt): ")
    tempos_execucao = []

    try:
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                match = re.search(r'Tempo de execu\S+: (\d+\.?\d*)s', linha)
                if match:
                    tempos_execucao.append(float(match.group(1)))
        
        if not tempos_execucao:
            print("Nenhum tempo de execução encontrado no arquivo.")
            return

        media = np.mean(tempos_execucao)
        desvio_padrao = np.std(tempos_execucao)

        print(f"\nResultados da Análise:")
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

analisar_logs()
