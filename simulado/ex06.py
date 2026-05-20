def potencia(b, exp):

    if exp == 0:
        return 1

    return b * potencia(b, exp - 1)

result = potencia(2,10)

print(result)
