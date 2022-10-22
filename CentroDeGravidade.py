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

def verificaCentro(M): #isso da certo(apenas para linhas)
    indiceL = 1
    indiceC = 1
    menorL = 0
    menorC = 0
    contL = 0
    contC = 0
    for i in range(1,len(M)-1): #i que percorre cada linha, menos a primeira e a última
        somaL = []
        for j in range(1,len(M)-1):# para somar linhas que não são do indice
            if i != j:
                
                somaL += M[j] #soma em uma lista todos os elementos menos o que estiver com o índice
        
        somaL = sum(somaL)
        
        if i == 1: #para 1ª comparação
            menorL = somaL
        elif somaL < menorL: 
            menorL = somaL
            indiceL = i+1
        elif somaL == menorL:
            contL += 1
            if contL == len(M)-3:
                indiceL = 'X'

    for i in range(1, len(M[0])): #i que percorre cada coluna, menos a primeira e a última
        somaC = []
        for j in range(1, len(M[0])):
            coluna = [0]*len(M)

            for k in range(len(M)): #faz uma lista com a coluna
                coluna[k] = M[k][i]

            if i != j:

                somaC = sum(coluna)
            
            if i == 1:
                menorC = somaC
            elif somaC < menorC:
                menorC = somaC
                indiceC = i+1

            elif somaC == menorC:
                contC += 1
                if contC == len(M)-3:
                    indiceC = 'X'
                
            
                
                
                
    return indiceL, indiceC


def main():
    arquivo = leArquivo('texto.txt')
    imprimeMatriz(arquivo)

    print('Centro: ', '(', verificaCentro(arquivo)[0],',',verificaCentro(arquivo)[1],')')
    
main()
