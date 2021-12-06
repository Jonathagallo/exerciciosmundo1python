#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
maximo = max(p, s, t)
minimo = min(p, s, t)

print(f'O menor valor digitado foi {minimo}')
print(f'O maior valor digitado foi {maximo}')