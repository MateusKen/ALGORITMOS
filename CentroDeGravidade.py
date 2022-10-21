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
    indice = 1
    menor = 0
    for i in range(1,len(M[0])-1): #i que percorre cada linha, menos a primeira e a última
        soma = []
        for j in range(1,len(M)-1):
            if i != j:
                
                soma += M[j] #soma em uma lista todos os elementos menos o que estiver com o índice
            print(soma)
        soma = sum(soma)
        if i == 1: #para 1ª comparação
            menor = soma
        elif soma < menor: 
            menor = soma
            indice += i
            
    return indice


def main():
    arquivo = leArquivo('asda.txt')
    imprimeMatriz(arquivo)
    print('Centro: ', '(', verificaCentro(arquivo),')')
    
main()
