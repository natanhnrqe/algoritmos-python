segundos = int(input('Digite o tempo de duração em segundos: '))

horas= int(segundos / 3600)
totSegundos = segundos % 3600
minutos = int(totSegundos / 60)
restSegundos = totSegundos % 60

print("==Tempo de conclusão do evento==")

if (horas == 1):
    print(f"{horas} hora, {minutos} minutos e {restSegundos} segundos")
else:
    print(f"{horas} horas, {minutos} minutos e {restSegundos} segundos")