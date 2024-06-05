# Ex3) b -
preco = 50
vendas = 800
receita = vendas*preco

while preco < 115:
    preco += 5
    vendas -= 20
print(f"A o preço de R$115 haverá: {vendas}")