alturas = []
idades = []

for i in range(2):
    altura = int(input("A altura: "))
    idade = int(input("A idade: "))
    alturas.append(altura)
    idades.append(idade)


print(f"Alturas: {alturas}")
print(f"Idades: {idades}")

alturas.reverse()
idades.reverse()

print(f"Alturas: {alturas}")
print(f"Idades: {idades}")


