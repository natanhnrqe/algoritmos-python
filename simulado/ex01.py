def somar_pares(n):
    soma = n

    if n < 2:
        return soma

    if n % 2 != 0:
        n = n - 1
        soma = n

    n -= 2
    return soma + somar_pares(n)

result = somar_pares(10)

print(result)