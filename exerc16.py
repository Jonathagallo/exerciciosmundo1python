#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input('Qual o valor?: '))
print (f'A porção inteira de {num} é {math.trunc(num)}')