import random



altura = [random.randint(155,200) for _ in range(30)]
idade = [random.randint(9,15) for _ in range(30)]


# for i in range(30):
#     print(f"--- Aluno {i+1} ---")
#     idades.append(int(input("Idade: ")))
#     alturas.append(float(input("Altura: ")))

media = sum(altura) / len(altura)

alunosEst = [i for i in range(30) if idade[i] > 13 and altura[i] < media]

print(f"Media de altura: {media}")
print(f"Alunos: {len(alunosEst)}")

