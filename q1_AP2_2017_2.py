import math




def pontosDeMaiorDistancia(nomeArquivo):

    with open(nomeArquivo, "r") as entrada:

        quantPontos = entrada.readline()
        quantPontos = int(quantPontos)

        if quantPontos == 0:
            print("Arquivo vazio!!!")
        else:
            posicao = entrada.tell()
            origem = lerPonto(entrada)

            # No início, a origem e o destino são a mesma tupla
            destino = origem

            # distância inicial é zero
            maiorDistancia = 0

            # voltando à posição do primeiro ponto do arquivo
            entrada.seek(posicao)

            for i in range(quantPontos):
                ponto1 = lerPonto(entrada)
                # salva a posição para o próximo ponto que será
                # considerado origem
                posicao = entrada.tell()
                for j in range(i+1, quantPontos):
                    ponto2 = lerPonto(entrada)

                    distancia = calcularDistancia(ponto1, ponto2)

                    if distancia > maiorDistancia:
                        maiorDistancia = distancia
                        origem = ponto1
                        destino = ponto2

                # navega para o próximo ponto que será considerado
                # origem no arquivo.
                entrada.seek(posicao)

            # imprimir resultados
            print("Pontos mais distantes:", origem, "e", destino,
                  "com distância = %.2f" % maiorDistancia)

    return None


def calcularDistancia(ponto1, ponto2):
    #p[0] == coordenada x
    #p[1] == coordenada y
    #dist = (expressao) ** (1/2) == raiz quadrada
    dist = math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)
    return dist


def lerPonto(arq):
    linha = arq.readline()
    x, y = linha.split()

    # as duas linhas acima poderiam ser
    #x, y = arq.readline().split()

    x = int(x)
    y = int(y)
    # x, y = (int(x), int(y))

    return (x, y)

# ------------------ programa principal ----------------- #


nomeArquivo = input()

pontosDeMaiorDistancia(nomeArquivo)
