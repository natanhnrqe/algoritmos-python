import random

def embaralhar(palavra):
    palavra = palavra.lower()

    caracter = list(palavra)
    random.shuffle(caracter)

    embaralhado = "".join(caracter)

    return embaralhado

texto = embaralhar("cavalo")

print(texto)