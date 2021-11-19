 #Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
 
medida = float(input('Digite uma distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print(f'A medida de {medida} metros corresponde a {mm} milimetros, \n à {cm} centimetros,\n à {km} kilometros')
