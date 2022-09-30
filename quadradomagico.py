def leArquivo(arquivo):
    arq = open(arquivo, 'r')
    tamanho = arq.readline()
    tamanho = tamanho.rstrip()
    tamanho = int(tamanho)
    vetLinhas = [0]*tamanho
    for i in range(tamanho):
        linha = arq.readline()
        linha = linha.rstrip()
        vetLinha = linha.split(' ')
        for j in range(tamanho):
            vetLinha[j] = int(vetLinha[j])
        vetLinhas[i] = vetLinha
    return vetLinhas

def imprimeMatriz(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(' ', M[i][j],' ', end='')

        print('\n')

def verificaQuadrado(M):
    somaLinha = 0
    somaColuna = 0
    for i in range(len(M)): #para linha
        for j in range(len(M)):

    for i in range(len(M)): #para coluna
        for j in range(len(M)):

    for i in range(len(M)): #para diagonal
        for j in range(len(M)):

def main():
    arquivo = leArquivo('quadradomagico.txt')
    imprimeMatriz(arquivo)
    é = verificaQuadrado(arquivo)
    if not é:
        print('Não é quadrado mágico')
    else:
        print('É quadrado mágico')
    arquivo.close()

main()
