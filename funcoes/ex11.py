def formatarData(data):

    dataBreak = data.split("/")

    if len(dataBreak) == 3:
        dia = int(dataBreak[0])
        mes = int(dataBreak[1])
        ano = int(dataBreak[2])

        return f"Dia: {dia}\nMês: {mes}\nAno:{ano}"

    return null

data = formatarData("11/09/2022")
print(data)