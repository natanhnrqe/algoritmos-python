vendas = [500, 1200, 2500, 3500, 5100, 6800, 8200, 9500, 10500, 15000]
contVend = [0] * 9

for v in vendas:
    salario = 200 + (0.09 * v)

    indice = int((salario - 200) / 100)


    if indice > 8:
        indice = 8

    contVend[indice] += 1

print("Contagem por faixa:", contVend)