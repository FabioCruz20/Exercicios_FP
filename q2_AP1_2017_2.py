

def fatorial_duplo(n):

    # pensar na condição de parada
    if n == 1:
        return 1
    else:
        return n * fatorial_duplo(n - 2)


# apenas um bônus: cálculo do fatorial simples recursivo

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

# --------------- programa principal ---------------- #

numero = int(input())

print("O fatorial de {0:d} é {1:d}".format(numero, fatorial(numero)))
#print("O fatorial de %d é %d" % (numero, fatorial(numero)))

while numero != -1:

    if numero % 2 == 0:
        print("O número", numero, "é par")
        #print("O número %d é par" % numero)
        #print("O número {0:d} é par".format(numero))
    else:
        result = fatorial_duplo(numero)
        print("O fatorial duplo de", numero, "é", result)
        #print("O fatorial duplo de", numero, "é", fatorial_duplo(numero))

    numero = int(input())
