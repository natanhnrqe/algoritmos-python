
def quadradoMagico(matriz):
    somaS = []
    somaDia = 0

    for l in range(3):
        soma = 0

        for c in range(3):
            if l == c:
                somaDia +=matriz[l][c]

            soma += matriz[l][c]

        somaS.append(soma)
    somaS.append(somaDia)

    if somaS.count(somaS[0]) == len(somaS):
        print("Eh um quadrado magico")
        for i in range(3):
            print(f"{matriz[i]} = {somaS[i]}")
        print(f"[{matriz[0][0]}, {matriz[1][1]}, {matriz[2][2]}] = {somaS[0]} ")


matriz = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

quadradoMagico(matriz)
