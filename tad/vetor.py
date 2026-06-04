
from tad.registro import RegistroCelular

## Class de criação e manipulação do Vetor

class cVetor:

    def __init__(self, n):
        
        self.capacidade = n
        self.numObjs = 0

        self.vet = [None] * n

    ## Adicionar Informação do Registro (IMEI)


    def insere(self, registro):
        if self.numObjs < self.capacidade:
            self.vet[self.numObjs] = registro
            self.numObjs += 1

    ## Pegar informação do Registro (IMEI) pela posição

    def getRegistro (self, pos):
        if pos >= 0 and pos < self.numObjs:
            return self.vet[pos]
        return -1
    
    ## Alterar informação do Registro (IMEI) pela posição

    def setRegistro(self, pos, registro):
        if pos >= 0 and pos < self.capacidade:
            self.vet[pos] = registro
        else:
            return -1
