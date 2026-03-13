dias = int(input('Quantos "dias" de idade você tem: '))

anos= int(dias / 365)
dias = dias % 365
meses = int(dias / 30)
restDias = dias % 30


print(f"Você tem {anos} anos, {meses} meses e {restDias} dias de vida!!!!")
