#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parde: '))
area = larg * alt
print(f'Sua parede tem a dimensao de {larg} x {alt} e sua area é de {area}m²')
tinta = area / 2
print(f'Para pintar essa parede voce precisara de {tinta}l de tinta')