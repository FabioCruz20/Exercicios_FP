import random

def lerDimensoes():
    linhas = int(input("Digite a quantidade de linhas: "))
    colunas = int(input("Digite a quantidade de colunas: "))

    return linhas, colunas


def criarMatriz(quantLinhas, quantColunas):

    # cria lista vazia chamada de matriz
    matriz = []
    for i in range(quantLinhas):

        # cria lista vazia chamada de linha
        linha = []
        for j in range(quantColunas):
            #linha.append(random.randint(-10, 10))
            numero = random.randint(-10, 10)
            linha.append(numero)

        # adicionando a linha preenchida à matriz.
        # Em python, uma matriz é uma lista de listas
        matriz.append(linha)

    # retornar a matriz preenchida
    return matriz


def imprimir(matriz, linhaI, linhaF, colunaI, colunaF):

    for i in range(linhaI, linhaF):
        for j in range(colunaI, colunaF):
            print(matriz[i][j], end=" ")
        print() # quebra de linha na tela
    return None


def imprimir2(matriz,linhaI, linhaF, colunaI, colunaF):

    for indLinha in range(linhaI, linhaF):
        for indColuna in range(colunaI, colunaF):
            print(matriz[indLinha][indColuna], end=" ")
        print()
    return None


# ------- programa principal -------- #

linhas, colunas = lerDimensoes()

if linhas < 3 or colunas < 3:
    print("A matriz é muito pequena")
else:
    matriz = criarMatriz(linhas, colunas)
    imprimir(matriz, 0, linhas, 0, colunas)

    print()
    print("Sub-matrizes")
    for indLinha in range(linhas - 3 + 1):
        for indColuna in range(colunas - 3 + 1):
            imprimir(matriz, indLinha, indLinha + 3, indColuna, indColuna + 3)
            print()


