#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('Qual velocidade voce estava ? : '))
if velocidade >= 80:
  multa = velocidade - 80
  multa = multa * 7
  print(f'Voce estava a {velocidade}Km/h e foi multado no valor de R${multa}')
else:
 print('Voce estava dentro do limite e nao foi multado')
