num = [int(input("Numeros: ")) for _ in range(20)]

par = [n for n in num if n % 2 == 0]
impar = [n for n in num if n % 2 != 0]

print(f"Todos: {num} \nPares: {par} \nImpares: {impar}")