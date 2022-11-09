#NOME: MATEUS KENZO IOCHIMOTO TIA: 32216289
'''
(1)
Escreva uma função que receba dois vetores (A[] e B[])
já ordenados em ordem crescente e ambos possuem o mesmo tamanho.
A sua função imprime a INTERSECÇÃO entre os dois vetores em ordem crescente,
ou seja, os elementos em comum entre os vetores A[] e B[].
Considere que os vetores não contêm valores duplicados.
A função deve ter deve ter complexidade O(n+m), ou seja,
o tamanho do vetor A[] e do vetor B[].
'''

def interseccao(A, B):
    inters = []
    for i in range(len(A)):
        if A[i] in B: # passa um for que confere se cada elemento de A está em B
            inters.append(A[i]) # uma comparação para cada i
    return inters

'''
(2)
Repita o exercício anterior, agora deve ser impresso os elementos
que estão em A[] mas não estão em B[]. A função deve ter deve ter
complexidade O(n), ou seja, o tamanho dos vetores.
'''

def AbutnotB(A,B):
    aux = []
    for i in range(len(A)):
        if A[i] not in B: # passa um for que confere se cada elemento de A está em B
            aux.append(A[i]) # uma comparação para cada i
    return aux

'''
(3)
Dado um vetor com números pares e ímpares, escreva uma função para colocar
todos os números pares à frente no vetor e os ímpares ao final. Você não pode
usar outro vetor como área auxiliar. A função deve ter deve ter complexidade O(n),
ou seja, o tamanho do vetor V[].
'''

def parPrimeiroimparUltimo(vet):
    par = 0 # conta quantos pares já foram contados
    p = 0 
    vet = sorted(vet) # obs: só funciona se os elementos estiverem em ordem crescente
    for i in range(len(vet)):
        if vet[i]%2 == 0:
            p = vet[par] # guarda o primeiro elemento, depois dos pares
            vet[par] = vet[i]
            vet[i] = p
            par += 1
    # obs: esse algoritmo só deixa os pares em ordem crescente, os ímpares não
    return vet
         

def main():
    A = [1,2,3,4,5]
    B = [2,4,5,6,8]
    C = [1,2,5,7,4,9,14,16]
    print(interseccao(A,B))
    print(AbutnotB(A,B))
    print(parPrimeiroimparUltimo(C))
main()
