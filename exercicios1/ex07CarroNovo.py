custoFabrica = float(input("Qual preço de fábrica do carro: "))


imposto = custoFabrica * 0.45
percDistribuidor = custoFabrica * 0.28

carroNovo = custoFabrica + imposto + percDistribuidor

print(f"Imposto: R${imposto:.2f}")
print(f"Percentual distribuidor: R${percDistribuidor:.2f}")
print(f"O carro novo vai sair por R${carroNovo:.2f}")
