import random

def geraVetor(n):
    v = [0]*n
    for i in range(n):
        v[i] = random.randint(0,100)
    #print(v)
    return v

def buscalinear(elem, vet):
    i = 0
    while i < len(vet):
        if vet[i] == elem:
            return i
        i += 1

    return -1

def buscaordenada(elem, vet):
    ordenado = sorted(vet)
    i = 0
    while i < len(vet) and ordenado[i] <= elem:
        if ordenado[i] == elem:
            return i
        i += 1
    return -1

def buscabinaria(elem, vet): 
    ordenado = sorted(vet)
    print(ordenado)
    i = 0
    f = len(vet)-1
    while i <= f:
        m = (i + f)//2
        if ordenado[m] == elem:
            return m
        elif ordenado[m] < elem:
            i = m + 1
        else:
            f = m -1
    return -1
    
def main():
    vetor = geraVetor(100)
    elemB = int(input())
    
    #print('\n',buscaordenada(elemB, vetor))
    #print('\n',buscalinear(elemB, vetor))
    print('\n',buscabinaria(elemB, vetor))
main()
