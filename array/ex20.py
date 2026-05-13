salarios = []

print("Projeção de Gastos com Abono")
print("============================")


while True:
    valor = float(input("Salário: "))
    if valor == 0:
        break
    salarios.append(valor)

print("\nSalário - Abono")

total_abonos = 0
minimo_pago = 0
maior_abono = 0

for s in salarios:
    abono = s * 0.20
    if abono < 100:
        abono = 100
        minimo_pago += 1

    if abono > maior_abono:
        maior_abono = abono

    total_abonos += abono
    print(f"R$ {s:>8.2f} - R$ {abono:>8.2f}")

print(f"\nforam processados {len(salarios)} colaboradores")
print(f"Total gasto com abonos: R$ {total_abonos:.2f}")
print(f"Valor mínimo pago a {minimo_pago} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_abono:.2f}")