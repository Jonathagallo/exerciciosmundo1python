#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
temp = float(input('Qual a temperatura?: '))
f = ((9 * temp) / 5) + 32
print(f'A temperatura de {temp}°C, corresponde a {f}°F')