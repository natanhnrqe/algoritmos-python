num = [int(input("Numeros: ")) for i in range(5)]
soma = 0
mult = 1

for x in num:
    soma += x
    mult *= x

print(f"Numeros: {num}")
print(f"Soma: {soma}")
print(f"Mult: {mult}")
