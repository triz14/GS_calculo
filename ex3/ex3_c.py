# Ex3) c -
preco = 50
vendas = 800
receita = preco * vendas

while receita < 50000:
    preco += 5
    vendas -= 20
    receita = vendas*preco
print(f"Para ter uma receita de R$50000 o preço correto do ingresso seria {preco}")