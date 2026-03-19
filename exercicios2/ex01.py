print(f"===================================================\n"
      f"CALCULADORA DE IMPOSTO DE RENDA(CUIDADO COM O LEAO)")



salBr = float(input("Digite seu sálario: "))
numDep = int(input("Digite o número de dependentes: "))
pensao = float(input("Coloque o valor que voce recebe da pensão alimenticia(caso necessário): "))

totDed = 0


resp = input("Deseja adicionar outras deducoes(s/n)?").lower()
while (resp != "n"):
    novaDed = (float(input("Digite a deducões: ")))
    totDed += novaDed
    resp = input("Deseja adicionar outras deducoes(s/n)?").lower()



faixaPercent = [0, 0.075, 0.15, 0.225, 0.275]

baseCalc = salBr - ((numDep * 189.59) + pensao + totDed)

imposto = 0

if baseCalc <= 1903.98:
    imposto = baseCalc * faixaPercent[0]
    faixaNome = "Faixa 1 (Isento)"

elif 1903.98 < baseCalc <= 2826.65:
    imposto = baseCalc * faixaPercent[1]
    faixaNome = "Faixa 2 (7,5%)"

elif 2826.65 < baseCalc <= 3751.05:
    imposto = baseCalc * faixaPercent[2]
    faixaNome = "Faixa 3 (15%)"

elif 3751.05 < baseCalc <= 4664.68:
    imposto = baseCalc * faixaPercent[3]
    faixaNome = "Faixa 4 (22,5%)"

elif 4664.68 < baseCalc:
    imposto = baseCalc * faixaPercent[4]
    faixaNome = "Faixa 5 (27,5%)"

else:print("Numero invalido")

salLiq = baseCalc - imposto


print(f"====================================================\n"
      f"Imposto a pagar: {imposto:.2f}\n"
      f"====================================================\n"
      f"Faixa IRPF: {faixaNome}\n"
      f"====================================================\n"
      f"Valor liquido: {salLiq:.2f}\n"
      f"====================================================")
