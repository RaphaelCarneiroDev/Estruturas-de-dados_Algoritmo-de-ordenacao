from tad.vetor import cVetor
from tad.registro import RegistroCelular

def countingSort(v, exp):

    vContagem = [0] * 10 ## Vetor de contagem, de 0 a 9 digitos

    vAuxiliar = cVetor(v.numObjs) ## Vetor auxiliar, para adicionar os números ordenados

    for i in range(v.numObjs):

        registro = v.getRegistro(i) ## Pega o registro no indice do range
        imei = int(registro.imei) ## Pega somente o IMEI e transforma em int
        digito = (imei // exp) % 10 ## pega o proximo digito a ser analisado

        vContagem[digito] += 1 ## Adiciona a contagem de quantas vezes este número ja apareceu

    for i in range(1, 10): ## looping para acumular os números para saber a posição
        vContagem[i] += vContagem [i - 1]
    
    for i in range(v.numObjs - 1, - 1, - 1): ## Percorrer o vetor de trás pra frente
        
        registro = v.getRegistro(i)
        imei = int(registro.imei)
        digito = (imei // exp) % 10
        pos = vContagem[digito] - 1

        vAuxiliar.setRegistro(pos, registro)

        vContagem[digito] -= 1
    
    vAuxiliar.numObjs = v.numObjs

    for i in range(v.numObjs): ## Copiar no Vetor Original
        v.setRegistro(i, vAuxiliar.getRegistro(i))



##
## exp é a casa decimal que voce quer pegar do número:
## exemplo: 1234
## exp = 1
## vai pegar o número 1234 dividir por 1 = 1234
## dividir por 10 e pegar o resto = 4
## exp = 10
## vai pegar a dezena, 1234 // 10
## 123 % 10 = 3
##