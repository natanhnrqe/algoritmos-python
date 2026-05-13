modelos = []
consumos = []

print("Comparativo de Consumo de Combustível")

for i in range(5):
    print(f"Veículo {i + 1}")
    modelos.append(input("Nome: "))
    consumos.append(float(input("Km por litro: ")))

print("\nRelatório Final")

mais_economico = ""
menor_consumo = 0  # Na verdade, queremos o MAIOR km/l

for i in range(5):

    litros_1000km = 1000 / consumos[i]
    custo = litros_1000km * 2.25

    print(f" {i + 1} - {modelos[i]:<10} - {consumos[i]:>4.1f} - {litros_1000km:>6.1f} litros - R$ {custo:>6.2f}")


    if consumos[i] > menor_consumo:
        menor_consumo = consumos[i]
        mais_economico = modelos[i]

print(f"O menor consumo é do {mais_economico}.")