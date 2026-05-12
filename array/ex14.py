print("=" * 10, "Iremos fazer 5 perguntas responda com s(sim) ou n(nao)", "=" * 10)
perguntas = ["Telefonou para a vítima? ", "Esteve no local do crime? ", "Mora perto da vítima? ",
            "Devia para a vítima? ", "Já trabalhou com a vítima? "]
cont = 0
for i in range(5):
    resp = input(perguntas[i]).lower()
    if  resp == "s":
        cont += 1
    else:
        continue

if cont == 2:
    print("Voce eh suspeito do crime")
elif 3 <= cont < 4:
    print("Voce eh cumplice")
elif cont == 5:
    print("ASSASINO")
