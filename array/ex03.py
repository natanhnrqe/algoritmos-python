

notas = [float(input(f" {i + 1} nota do aluno: ")) for i in range(4)]

media = sum(notas) / len(notas)

print(f"Notas: {notas} \n"
      f"Media: {media}")
