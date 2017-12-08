# Função que recebe um arquivo aberto,
# lê uma linha, e a transforma em tupla de inteiros

def obterPonto(arq):
    linha = entrada.readline()
    if linha != "":
        linha = linha.split()
        linha[0] = int(linha[0])
        linha[1] = int(linha[1])
    return tuple(linha)


# Função que recebe duas listas que representam
# pontos e calcula a distância entre eles

def calcularDistancia(ponto1, ponto2):
    from math import sqrt
    distancia = sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)
    return distancia

# ----------------- programa principal ---------------- #

nomeArquivo = input()

with open(nomeArquivo) as entrada:
    maiorDistancia = 0

    quantPontos = entrada.readline()
    quantPontos = int(quantPontos)

    if quantPontos == 0:
        print("Arquivo vazio!!!")
    else:
        pontoOrigem = ()
        pontoDestino = ()
        for i in range(quantPontos - 1):
            ponto1 = obterPonto(entrada)
            posicao = entrada.tell()
            #print("Ponto1:", ponto1)
            #print("Posição do cursor:", posicao)
            for j in range(i + 1, quantPontos):
                ponto2 = obterPonto(entrada)
                #print("Ponto2:", ponto2)
                #posicao1 = entrada.tell()
                #print("Posição do cursor:", posicao1)
                distancia = calcularDistancia(ponto1, ponto2)

                if distancia > maiorDistancia:
                    maiorDistancia = distancia
                    pontoOrigem = ponto1
                    pontoDestino = ponto2

            entrada.seek(posicao)

        print("Pontos mais distantes:", pontoOrigem, "e",
              pontoDestino, "com distância = %.2f" % maiorDistancia)











