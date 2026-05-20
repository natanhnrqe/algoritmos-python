def somar_pares(n):

    if n < 2:
        return n

    if n % 2 != 0:
        n = n - 1

    return n + somar_pares(n - 2)

result = somar_pares(4)

print(result)