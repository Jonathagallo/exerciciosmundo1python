#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
nome = str(input('Qual seu nome: '))
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))