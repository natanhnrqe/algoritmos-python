sistemas = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
votos = [0] * 6
total_votos = 0

print("Enquete: Qual o melhor Sistema Operacional para uso em servidores?")
print("1- Windows Server | 2- Unix | 3- Linux | 4- Netware | 5- Mac OS | 6- Outro")

while True:
    try:
        voto = int(input("Voto (0 para sair): "))
        if voto == 0:
            break
        if voto < 1 or voto > 6:
            print("Valor inválido! Informe um valor entre 1 e 6.")
            continue

        votos[voto - 1] += 1  # Ajuste de índice: opção 1 vai para índice 0
        total_votos += 1
    except ValueError:
        print("Por favor, digite um número inteiro.")


print(f"\n{'Sistema Operacional':<19} {'Votos':<5} {'%'}")
print("-" * 19, "-" * 5, "---")

vencedor_nome = ""
vencedor_votos = 0

for i in range(len(sistemas)):
    percentual = (votos[i] / total_votos * 100) if total_votos > 0 else 0
    print(f"{sistemas[i]:<19} {votos[i]:<5} {percentual:.0f}%")

    if votos[i] > vencedor_votos:
        vencedor_votos = votos[i]
        vencedor_nome = sistemas[i]

print("-" * 19, "-" * 5)
print(f"Total {total_votos}")

if total_votos > 0:
    perc_vencedor = (vencedor_votos / total_votos * 100)
    print(f"\nO Sistema Operacional mais votado foi o {vencedor_nome}, com {vencedor_votos} votos, "
          f"correspondendo a {perc_vencedor:.0f}% dos votos.")