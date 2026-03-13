medMat = float(input("Digite a sua nota de Matemática: "))
medPort = float(input("Digite a sua nota de Português: "))
medHis = float(input("Digite a sua nota de História: "))

mediaPond = ((medHis * 2) + (medPort * 3) + (medMat * 5 )) / (2 + 3 + 5)

print(f"Sua média é: {mediaPond}")
