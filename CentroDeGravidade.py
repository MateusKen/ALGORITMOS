'''
NOME: MATEUS KENZO IOCHIMOTO TIA: 32216289
'''

'''
Alguns algoritmos para reconhecimento ótico de caracteres compara a imagem escaneada com modelos de
caracteres perfeitos. Parte da dificuldade com tais comparações é decidir onde começar a comparação. Isto
se deve ao fato de que as imagens escaneadas estão sujeitas a distorções, resultando em mudanças no
tamanho, posição e orientação. Um procedimento que algumas vezes é utilizada para lidar com essas
mudanças na posição é “casar” o centro de gravidade do caractere escaneado com centro de gravidade do
modelo com o qual ele é comparado.

Para os nossos propósitos, um caractere escaneado será uma matriz retangular de números reais com
valores em uma escala de cinza. A escala de cinza tem valores entre 0,0 (representando uma região
totalmente branca) e 1,0 (representando uma região totalmente preta).

O centro de gravidade é um elemento particular de uma matriz. Suponha um centro de gravidade na iésima1
linha e j-ésima coluna, então a diferença entre a soma dos elementos das duas porções da matriz
acima e abaixo da i-ésima linha é mínima. Analogamente a diferença entre a soma dos elementos das duas
porções a esquerda e direita da j-ésima coluna é mínima.

O seu objetivo neste trabalho é escrever um programa que tenha como entrada uma sequência de
caracteres escaneados e determinar qual quais são os centros de gravidades das imagens.

Entrada
A entrada do seu programa deve ser realizada a partir de um arquivo texto com seguinte formato, no início
do arquivo teremos dois inteiros especificando a quantidade de linhas e colunas de uma matriz retangular,
em seguida os valores em ponto flutuante (de 0.0 até 1.0 com precisão de uma casa decimal)
representando a escala de cinza do caractere escaneado. Um par de zeros indica que não temos mais
imagens para serem analisadas.

Importante: considere que a matriz sempre terá no mínimo 3 linhas e 3 colunas. E para facilitar a conversão
dos números reais lidos usaremos ponto (“.”) ao invés de vírgula (“,”) para separar a parte inteira da parte
decimal dos números.

Saída
Para cada caractere deverá mostrar no monitor a linha e a coluna correspondente ao centro de gravidade.
Se houver mais de um centro de gravidade, apresente somente o primeiro encontrado. Note que na saída é
informado a posição do centro de gravidade, ou seja, 1ª, 2ª, 3ª ... linha e coluna onde foi encontrado o
centro de gravidade.



'''
def geraMatriz(t1, t2, arquivo): #t1= tamanho da linha, t2= tamanho da coluna #isso funciona
    vetLinhas = [0]*t1
    vetColunas = [0]*t2
    for i in range(t1):
        linha = arquivo.readline()
        linha = linha.rstrip()
        vetLinha = linha.split(' ')
        for j in range(t2):
            vetLinha[j] = float(vetLinha[j])
        vetLinhas[i] = vetLinha 
    return vetLinhas #não consegue ler as entradas do jeito pedido

def imprimeMatriz(M): #isso da certo
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(' ', M[i][j],' ', end='')
        print('\n')

def verificaCentro(M): #isso da certo
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
        
        if i == 1: #para 1ª comparação das linhas
            menorL = somaL
        elif somaL < menorL: 
            menorL = somaL
            indiceL = i+1
        elif somaL == menorL:
            contL += 1
            if contL == len(M)-3: #para comparações em que todas as linhas são iguais
                indiceL = 'X'

    for i in range(1, len(M[0])-1): #i que percorre cada coluna, menos a primeira e a última
        somaC = 0
        for j in range(1, len(M[0])-1):
            coluna = [0]*len(M)

            for k in range(len(M)): #faz uma lista com a coluna
                coluna[k] = M[k][i]

            if i != j:
                
                somaC += sum(coluna)
                

        if i == 1: # para 1ª comparação das colunas
            menorC = somaC
        elif somaC < menorC:
            menorC = somaC
            indiceC = i

        elif somaC == menorC: 
            contC += 1
            if contC == len(M)-3:#para comparações em que todas as colunas são iguais
                indiceC = 'X'
                
    return indiceL, indiceC


def main():
    arquivo = open('texto.txt', 'r')
    vetT = []
    while True:
        tamanho = arquivo.readline()
        tamanho = tamanho.rstrip()
        
        vetT = tamanho.split(' ')
        for i in range(len(vetT)):
            vetT[i] = int(vetT[i])
            
        if vetT == [0,0]: 
            break
        
        else:
            arq = geraMatriz(vetT[0], vetT[1], arquivo)
            imprimeMatriz(arq)
            print('Centro: ', '(', verificaCentro(arq)[0],',',verificaCentro(arq)[1],')')
        
    arquivo.close()
    
main()
