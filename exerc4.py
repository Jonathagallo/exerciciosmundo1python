# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'Só tem espaços?{a.isspace()}')
print(f'É um numero? {a.isnumeric()}')
print(f'É alfabetico? {a.isalpha()}')
print(f'Éalphanumerico? {a.isalnum()}')
print(f'Esta em maisculas? {a.isupper()}')
print(f'Esta em minisculas? {a.islower()}')
print(f'Esta capitalizado? {a.istitle()}')