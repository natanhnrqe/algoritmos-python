import random

numRandom = [random.randint(-1, 100) for j in range(10000)]

nums = numRandom
numsAcima = []
numsAbaixo7 = []
for _ in range(10000):
    # num = int(input("Digite numeros ai: "))

    if nums[_] >= 0:
        nums.append(nums[_])
    else:
        break

soma = sum(nums)
media = soma / len(nums)

print(f"Quantidade de valores que foram lidos: {len(nums)}")
print(f"Todos os valores na ordem em que foram informados: {nums}")
print(f"Todos os valores na ordem inversa à que foram informados: {nums.reverse()}")
print(f"Soma dos valores: {soma}")
print(f"Média dos valores: {media}")

for n in nums:
    if n > media:
        numsAcima.append(n)
    elif n < 7:
        numsAbaixo7.append(n)

print(f"Quantidade de valores acima da média: {len(numsAcima)}")
print(f"Quantidade de valores abaixo de sete: {len(numsAbaixo7)}")

print("ENCERRANDO..................")
