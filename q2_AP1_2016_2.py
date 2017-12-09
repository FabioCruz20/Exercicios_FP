

def converter(numDecimal, base):
    # dígitos necessários para converter até a base 16
    #digitos = "0123456789ABCDEF"

    #dígitos necessários para converter até a base 9
    digitos = "012345678"

    # condição de parada: numDecimal < base
    if numDecimal < base:
        return str(numDecimal)

    else:
        return converter(numDecimal // base, base) + digitos[numDecimal % base]


# --------------- programa principal -------------- #

numeroDecimal = int(input())

while numeroDecimal != -1:

    for base in range(2, 10):
        convertido = converter(numeroDecimal, base)
        print(convertido, end=" ")

    # adicionar uma quebra de linha
    print()

    numeroDecimal = int(input())
