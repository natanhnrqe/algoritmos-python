medias = []

for i in range(10):
    notas = [float(input(f"{j + 1} nota do {i + 1} aluno: ")) for j in range(4)]

    medias.append(sum(notas) / 4)

maior = [n for n in medias if n >= 7.0]


print(f"Acima da media: {len(medias)} alunos \n"
      f"Media: {medias}")