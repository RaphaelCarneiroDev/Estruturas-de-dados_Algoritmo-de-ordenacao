from tad.registro import RegistroCelular
from tad.vetor import cVetor

def lerArq(arquivo, v): ## Função para ler o arquivo designado
    arq = open(arquivo, "r")

    for linha in arq:
        linha = linha.strip()

        dados = linha.split(',')
        
        registro = RegistroCelular(dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])

        v.insere(registro)
        
    arq.close()