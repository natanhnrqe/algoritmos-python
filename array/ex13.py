
temp = [17, 9, 16, 21, 5, 12, 23, 0, 13, 6, 26, 24]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mediaTemp = sum(temp) / len(temp)


mesesAcima = [m for m in range(12) if temp[m] > mediaTemp]

print(f"Meses acima da media({mediaTemp:.0f}): ")
for a in mesesAcima:
    print(meses[a])




