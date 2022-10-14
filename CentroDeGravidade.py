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
Como exemplo, considere que a matriz abaixo representa o caractere “o” escaneado, o centro de
gravidade desta matriz está singularmente na 3ª linha, e 3ª coluna, pois a diferença entre a soma dos
elementos em cada porção da matriz informada, ignorando a terceira linha é 0,1 (as somas das porções
abaixo e acima são 5,55 e 5,65, respectivamente). A diferença entre a soma de cada porção da matriz
formada ignorando a terceira coluna é 0,0 (a soma de ambas as porções é 5,60).
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
Observações importantes:
Este trabalho deve ser desenvolvido em duplo (no máximo dois alunos), e devem ser seguidas as
Orientações para Desenvolvimento de Trabalhos Práticos disponível no Moodle. A entrega do trabalho
deve ser feita pelo Moodle (não serão aceitos trabalhos entregues via e-mail) e será avaliado de acordo
com os seguintes critérios:
• Funcionamento do programa;
• O programa deve estar na linguagem Python.
• O quão fiel é o programa quanto à descrição do enunciado;
• Identação, comentários e legibilidade do código;
• Clareza na nomenclatura de variáveis e funções;
• Não é permito métodos da classe List do Python, tais como insert(), pop(), remove(), index(),
append() entre outros, também não é permitido o uso de bibliotecas prontas tipo Numpy.
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

def verificaCentro(M): #isso ainda não da certo
    for i in range(1,len(M[0])-2): #i que percorre cada linha, menos a primeira e a última
        soma = sum(M[:i-1]) + sum(M[i+1:len(M)]) #é isso que eu preciso, mas isso não funciona
        return soma


def main():
    arquivo = leArquivo('texto.txt')
    imprimeMatriz(arquivo)
    soma = sum(arquivo[0])
    print(verificaCentro(arquivo))
    
main()
