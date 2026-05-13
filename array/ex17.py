while True:
    nome = input("Atleta (ou Enter para sair): ")
    if nome == "":
        break

    for i in range(5):
        distancia = float(input(f"Digite o {i + 1}º salto: "))
        saltos.append(distancia)

    print(f"\nAtleta: {nome}")


    for j in range(len(saltos)):
        print(f"{j + 1}º Salto: {saltos[j]} m")

    media = sum(saltos) / len(saltos)

    print(f"\nResultado final:")
    print(f"Atleta: {nome}")

    print(f"Saltos: {' - '.join(map(str, saltos))}")
    print(f"Média dos saltos: {media:.1f} m\n")