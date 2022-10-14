'''
NOME: MATEUS KENZO IOCHIMOTO TIA: 32216289 
'''
def leArquivo(arquivo): #isso da certo
    arq = open(arquivo, 'r')
    tamanho = arq.readline()
    tamanho = tamanho.rstrip()
    vetT = tamanho.split(' ')
    for i in range(len(vetT)):
        vetT[i] = int(vetT[i])
    vetLinhas = [0]*vetT[0]
    vetColunas = [0]*vetT[1]
    for i in range(vetT[0]):
        linha = arq.readline()
        linha = linha.rstrip()
        vetLinha = linha.split(' ')
        for j in range(vetT[1]):
            vetLinha[j] = float(vetLinha[j])
        vetLinhas[i] = vetLinha 
    return vetLinhas #não consegue ler as entradas do jeito pedido

def imprimeMatriz(M): #isso da certo
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(' ', M[i][j],' ', end='')

        print('\n')

def verificaCentro(M): #isso ainda não da certo (apenas para linhas)
    indice = 0
    menor = 10000000
    for i in range(1,len(M[0])-1): #i que percorre cada linha, menos a primeira e a última     
        j= 0
        soma1 = 0
        soma2 = 0
        while j < i:
            soma1 = soma1 + M[i][j]
            j +=1
        j = len(M[i])-1
        while j > i:
            soma2 = soma2 + M[i][j]
            j -= 1
        if menor > (soma1-soma2):
            menor = soma1-soma2
            indice = i+2
    return indice


def main():
    arquivo = leArquivo('texto.txt')
    imprimeMatriz(arquivo)
    soma = sum(arquivo[0])
    print(verificaCentro(arquivo))
    
main()
