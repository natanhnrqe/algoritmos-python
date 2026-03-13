from datetime import datetime

anos = int(input('Digite quantos "anos" de idade você tem: '))
meses = int(input('e quantos "meses" de idade você tem: '))
dias = int(input('e quantos "dias" de idade você tem: '))

print(f"Você tem {anos} anos, {meses} meses e {dias} dias de idade!!!")

diasAnos = anos * 365
diasMeses = meses * 30

idadeDias = diasAnos + diasMeses + dias

print(f"Sua idade em dias é: {idadeDias}!!!")

#Versao complementar

textoData = input("Digite a sua data de nascimento (dd/mm/aaaa): ")
nascimentoData = datetime.strptime(textoData, "%d/%m/%Y")
atualData = datetime.now()
diasVividos = (atualData - nascimentoData).days

print(f"Aproximadamente {diasVividos} dias vividos!!!")





