def is_positive(n):
    if n % 2 != 0 or n == 0:
        return "N"
    else:
        return "P"

n = int(input("Digite um numero: "))


resp = is_positive(n)
print(resp)