#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print(f'O angulo de {angulo} tem o seno de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O angulo de {angulo} tem o cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem o seno de {tangente:.2f}')