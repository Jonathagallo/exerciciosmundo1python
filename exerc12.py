#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual o preço do produto ?: '))
desconto = preco - (preco * 5 / 100)
print(f'O valor com desconto no produto é R${desconto}')