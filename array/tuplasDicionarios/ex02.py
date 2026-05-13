anos_luz = {"pc": 0.31, "al": 1, "ae": 63241.09, "ml": 525960.23, "sl": 31557609.92}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]

print("Unidades disponíveis:")
for u in unidades:
    print(f"- {u}")

valor = float(input("\nValor a ser convertido: "))
origem = input("Converter de (use a sigla): ").lower()
destino = input("Converter para (use a sigla): ").lower()

# Lógica: Valor / TaxaOrigem * TaxaDestino
valor_em_al = valor / anos_luz[origem]
valor_final = valor_em_al * anos_luz[destino]

print(f"Conversão: {valor} {origem} = {valor_final:.2f} {destino}")