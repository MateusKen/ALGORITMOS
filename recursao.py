def somaLista1(lista): #usando iteração
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def somaLista2(lista): #usando recursão
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somaLista2(lista[1:])

def somaLista3(lista): #usando sum()
    return sum(lista)

def fibonacci(n): #sequência de fibonacci
    if n < 1:
        return 0
    elif n < 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def buscaBinariaRec(elem, vet):
    ordenado = sorted(vet)
    i = 0
    f = len(vet)-1
    m = (i + f)//2
    print(ordenado)
    if ordenado[m] == elem:
        return elem
    elif ordenado[m] < elem:
        return buscaBinariaRec(elem, ordenado[m:])
    elif ordenado[m] > elem:
        return buscaBinariaRec(elem, ordenado[:m])
    else:
        return -1

def main():
    lista = [1,2,3,4]

    print(somaLista1(lista))
    print(somaLista2(lista))
    print(somaLista3(lista))
    print(fibonacci(800))
    print(buscaBinariaRec(5,lista))
main()
    
