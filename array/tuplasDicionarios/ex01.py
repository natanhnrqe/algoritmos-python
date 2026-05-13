estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
    'x-burguer': ['pao', 'hamburguer'],
    'x-salada': ['pao', 'hamburguer', 'tomate'],
    'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
    'x-egg': ['pao', 'hamburguer', 'ovo'],
    'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

print("--- Cardápio Boca Feliz ---")
for lanche in cardapio:
    print(f"- {lanche}")

while True:
    pedido = input("\nO que deseja pedir (0 para sair)? ").lower()
    if pedido == '0':
        break

    if pedido not in cardapio:
        print("Item não localizado no cardápio")
        continue

    ingredientes_necessarios = cardapio[pedido]
    possivel_fazer = True


    for ing in ingredientes_necessarios:
        if estoque.get(ing, 0) <= 0:
            print(f"Infelizmente acabou o {ing}")
            possivel_fazer = False


    if possivel_fazer:
        for ing in ingredientes_necessarios:
            estoque[ing] -= 1
        print(f"Um {pedido} saindo no capricho!!!")