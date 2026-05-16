import random


def lancar_dados():
    input("\nPressione Enter para lançar os dados...")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma = dado1 + dado2
    print(f"Dados: {dado1} + {dado2} = {soma}")
    return soma


# Primeira Jogada
print("--- JOGO DE CRAPS ---")
resultado = lancar_dados()

if resultado in [7, 11]:
    print("Natural! Você ganhou!")
elif resultado in [2, 3, 12]:
    print("CRAPS! Você perdeu!")
else:
    ponto = resultado
    print(f"Seu PONTO é {ponto}. Agora você deve tirá-lo novamente.")

    # Rodadas de Ponto
    while True:
        proximo_lancamento = lancar_dados()

        if proximo_lancamento == ponto:
            print("Você tirou seu Ponto novamente! Ganhou!")
            break
        elif proximo_lancamento == 7:
            print("Você tirou um 7 antes do Ponto... Perdeu!")
            break
        else:
            print("Continue tentando...")