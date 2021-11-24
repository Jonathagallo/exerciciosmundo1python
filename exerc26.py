#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('a letra a aparece {} vezes'.format(frase.count('A')))
print('a letra a aparece pela primeira vez na posiçao {}'.format(frase.find('A')+1))
print('a letra a aparece pela ultima vez na posiçao {}'.format(frase.rfind('A')+1))