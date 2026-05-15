def reverso(num):
    lista = [int(d) for d in str(num)]
    rev = []

    for i in range(len(lista) - 1, -1, -1):
        rev.append(lista[i])

    listInt = "".join(map(str, rev))
    return listInt


print(reverso(4321))







