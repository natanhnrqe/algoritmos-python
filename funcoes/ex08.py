def tamanho(num):
    lista = [int(d) for d in str(num)]
    size = 0
    for l in lista:
        size += 1
    return size

print(tamanho(1000))