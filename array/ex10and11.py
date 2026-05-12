import random

# para nao ficar dando input toda vez
arr1 = [random.randint(1,50) for _ in range(10)]
arr2 = [random.randint(1,50) for _ in range(10)]
arr3 = [random.randint(1,50) for _ in range(10)]

result = []

for i in range(len(arr1)):
    result.append(arr1[i])
    result.append(arr2[i])
    result.append(arr3[i])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
print(f"Array 3: {arr3}")
print(f"Resultado: {result}")