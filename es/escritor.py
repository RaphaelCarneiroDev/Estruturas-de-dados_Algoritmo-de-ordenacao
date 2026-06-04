

def escreverArq(Nome, v): ## Função para escrever os registros ordenados em .csv

    arq = open(Nome, 'w')

    for i in range(v.numObjs):
        registro = v.getRegistro(i)

        linha = (
            str(registro.imei) + ',' +
            registro.fabricante + ',' +
            registro.modelo + ',' +
            str(registro.ano) + ',' +
            str(registro.cpf) + ',' +
            str(registro.cep)
        )

        arq.write(linha + '\n')
    
    arq.close()