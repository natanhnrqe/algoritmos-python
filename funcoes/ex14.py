def retangulo(lines=1, colunas=1):

    lines = max(1, min(lines, 20))
    colunas = max(1, min(colunas, 20))

    # Se tiver apenas 1 coluna ou 1 linha, a lógica muda um pouco para não duplicar os cantos
    if colunas == 1:
        for _ in range(lines):
            print("+")
        return
    if lines == 1:
        print("+" + "-" * (colunas - 2) + "+")
        return


    print("+" + "-" * (colunas - 2) + "+")


    for _ in range(lines - 2):
        print("|" + " " * (colunas - 2) + "|")


    print("+" + "- " * (colunas - 2) + "+")

# Testando
retangulo(10, 8)