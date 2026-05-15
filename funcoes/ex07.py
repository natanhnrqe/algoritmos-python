def valorPagamento(valor, atraso):
    multa = 1.03
    atraso = atraso * 0.001
    juros = multa + atraso

    if atraso == 0:
        return valor

    return valor * juros

def printPagamentos():
    valores = []
    while True:
        valor = float(input("Digite o valor da prestacao:  "))
        atraso = float(input("Digite os dias de atraso(0 para nenhum atraso): "))

        liq = valorPagamento(valor, atraso)
        print(f"Valor a ser paga: R${liq:.2f}")

        valores.append(liq)

        if input("Deseja adicionar mais valores?(s/n) ") == "n":
            print("=" * 10, "RELATORIO GERAL", "=" * 10)
            for v in valores:
                print(f"R${v}", end= "\n")
            total = sum(valores)
            print(f"=" * (22 + len("RELATORIO GERAL")),
                  f"\nTotal de contas a pagar: R${total}")

            break


printPagamentos()
