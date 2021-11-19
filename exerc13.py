# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o valor do seu salario?: '))
novo = salario + (salario * 15 / 100)
print(f'O novo salario com o reajuste sera R${novo}')