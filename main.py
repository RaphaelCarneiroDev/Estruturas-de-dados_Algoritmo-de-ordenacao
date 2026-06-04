
import sys
from algoritmos.radixSort import radixSort
from es.leitor import lerArq
from es.escritor import escreverArq
from processo.remvDupli import removerDupli
from tad.vetor import cVetor


def main():

    args = sys.argv ## Usado para ler os arquivos tomando como parâmetro no terminal

    arquivos_entrada = [None] * len(args)
    qtd_arquivos = 0

    arquivo_saida = "saida.csv"

    i = 1
    while i < len(args):
        if args[i] == "-o": 
            arquivo_saida = args[i + 1]
            i += 2
        else:
            arquivos_entrada[qtd_arquivos] = args[i]
            qtd_arquivos += 1
            i += 1

    vetor = cVetor(1000000)

    total_lidos = 0

    for i in range(qtd_arquivos):
        arquivo = arquivos_entrada[i]
        lerArq(arquivo, vetor)
        print(f"Arquivo {arquivo} lido")

    total_lidos = vetor.numObjs

    radixSort(vetor)
    print("Ordenação concluída")

    vetor = removerDupli(vetor)
    print("Duplicatas removidas")

    escreverArq(arquivo_saida, vetor)

    print(f"\nArquivo final salvo em: {arquivo_saida}")

    print("\n=== ESTATÍSTICAS ===")
    print(f"Total lido: {total_lidos}")
    print(f"Total final: {vetor.numObjs}")
    print(f"Duplicados removidos: {total_lidos - vetor.numObjs}")


if __name__ == "__main__":
    main()




## python main.py (Get-ChildItem dados_teste/grande/*.csv) -o saida.csv
## Chamada para ler todos os arquivos de uma pasta (grande)