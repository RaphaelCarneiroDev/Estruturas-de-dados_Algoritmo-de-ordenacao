
from algoritmos.countingSort import countingSort

def radixSort(v):

    exp = 1

    for i in range(0, 15): ## Looping que roda os 15 digitos do IMEI por cada elemento do vetor
        countingSort(v, exp)
        exp *= 10

