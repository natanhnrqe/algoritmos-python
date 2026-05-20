
def somarMatrizes(matriz):
    soma = 0
    cont = 0

    for l in range(3):

        for c in range(3):

            if matriz[l][c] < 0:
                cont += 1

    return cont

matriz = [
    [1, 2, 3],  # Linha 0 -> coluna 0 é 1, coluna 1 é 2, coluna 2 é 3
    [4, -5, 6],  # Linha 1 -> coluna 0 é 4, coluna 1 é 5, coluna 2 é 6
    [7, 8, -9]   # Linha 2 -> coluna 0 é 7, coluna 1 é 8, coluna 2 é 9
]

result = somarMatrizes(matriz)
print(result)