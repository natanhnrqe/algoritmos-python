def somaImposto(taxa, custo):
    taxa = taxa / 100
    print(f"R${custo} | antes dos impostos")
    if input("Deseja ver o preco final com impostos?(s/n) ") == "s":
        custo += custo * taxa
        print(f"Com impostos do Governo Maldito fica: R${custo}")

somaImposto(50, 500)