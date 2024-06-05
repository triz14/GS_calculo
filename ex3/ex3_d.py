# Ex3) d -
preco = 50
vendas = 800
receita = preco * vendas

max_receita = receita
melhor_preco = preco

while True:
    preco += 5
    vendas -= 20
    nova_receita = vendas * preco

    if nova_receita > max_receita:
        max_receita = nova_receita
        melhor_preco = preco
    else:
        break

print("Maior Receita:", max_receita)
print("Melhor Preço:", melhor_preco)