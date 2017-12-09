

# dicionario[chave] = valor
# se a chave não existe, ela é criada.
# se a chave já existe, o valor associado a chave é trocado.


# ------------------- programa principal ------------------ #


# "r" é o modo padrão: leitura
with open("mensagens.txt", "r") as arqMensagens:
    traducoes = dict() # cria dicionário vazio

    # Lê primeira linha do arquivo para saber se está
    # vazio ou não
    # rstrip("\n") retira o(s) caractere(s) "\n" da exremidade
    # direita da string
    idioma = arqMensagens.readline().rstrip("\n")

    while idioma != "":
        # Lê mensagem associada ao idioma
        mensagem = arqMensagens.readline().rstrip("\n")

        # adiciona par chave-valor ao dicionário
        traducoes[idioma] = mensagem

        # atualiza a variável de controle para saber
        # se devemos sair do loop while ou não.
        idioma = arqMensagens.readline().rstrip("\n")


with open("clientes.txt") as arqClientes:

    nome = arqClientes.readline()

    while nome != "":

        # o valor de idioma é usado para acessar uma mensagem
        # no dicionário. Logo, o valor de idioma é uma chave
        # para o dicionário traducoes
        idioma = arqClientes.readline().rstrip("\n")

        # As três linhas de saída pedidas pelo enunciado da questão
        print(nome, end="")
        print(traducoes[idioma])
        print()

        nome = arqClientes.readline()






