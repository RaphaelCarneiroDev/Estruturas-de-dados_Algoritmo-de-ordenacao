from tad.vetor import cVetor


def removerDupli(v): ## função para remover duplicatas
    
    if v.numObjs == 0:
        return v

    vetorSemDupli = cVetor(v.numObjs) ## Cria um novo vetor sem as duplicatas
    primeiro = v.getRegistro(0) 
    vetorSemDupli.insere(primeiro) ## Sempre coloca o primeiro vetor e compara com o proximo

    for i in range(1, v.numObjs):

        atual = v.getRegistro(i)
        anterior = v.getRegistro(i - 1)

        if atual.imei != anterior.imei: ## Então se o vetor do indice [i] for igual ao do indice anterior: são duplicatas
            vetorSemDupli.insere(atual)
    
    return vetorSemDupli