def calcular_percentual(votos_jogador, total_votos):
    if total_votos == 0: return 0
    return (votos_jogador / total_votos) * 100


votos = [0] * 24
total_votos = 0

print("Enquete: Quem foi o melhor jogador?")

while True:
    try:
        num = int(input("Número do jogador (0=fim): "))
        if num == 0:
            break
        if num < 1 or num > 23:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")
            continue

        votos[num] += 1
        total_votos += 1
    except ValueError:
        print("Digite um número inteiro válido.")


resultado = f"Resultado da votação:\nForam computados {total_votos} votos.\n"
resultado += f"{'Jogador':<10} {'Votos':<10} {'%'}\n"

melhor_jogador = 0
max_votos = 0

for i in range(1, 24):
    if votos[i] > 0:
        perc = calcular_percentual(votos[i], total_votos)
        resultado += f"{i:<10} {votos[i]:<10} {perc:.1f}%\n"

        if votos[i] > max_votos:
            max_votos = votos[i]
            melhor_jogador = i

if total_votos > 0:
    perc_melhor = calcular_percentual(max_votos, total_votos)
    final = f"O melhor jogador foi o número {melhor_jogador}, com {max_votos} votos, correspondendo a {perc_melhor:.1f}% do total."
    resultado += final
    print(resultado)

    with open("resultado.txt", "w") as f:
        f.write(resultado)