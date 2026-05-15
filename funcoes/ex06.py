def convertionHour(hora, minuto):
    if hora > 12:
        hora -= 12
        minuto = minuto
        return f"{hora}:{minuto} P.M"
    return f"{hora}:{minuto} A.M"

def printHora():
    while True:
        print("===Conversor de datas===")
        hora = int(input("Digite a hora: "))
        minuto = int(input("Digite os minutos: "))

        tempo = convertionHour(hora, minuto)

        print(f"Conversao completa: {tempo}")

        if input("Deseja converter outro tempo?(s/n)") == "n":
            break

printHora()