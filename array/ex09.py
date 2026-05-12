import random

# para nao ficar dando input toda vez
arr = [random.randint(1,50) for _ in range(10)]

total = 0

for a in arr:
    total += a**2

print(arr)
print(f"A soma dos quadrados dos arrays eh: {total}")