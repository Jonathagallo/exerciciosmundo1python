#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


dia = float(input('Digite o numero de dias que o carro ficou alugado: '))
km = float(input('Digite o km rodado do carro alugado: '))

custo = (dia * 60 ) + (km * 0.15)

print(f'O valor a pagar pelo aluguel do carro é R${custo}')