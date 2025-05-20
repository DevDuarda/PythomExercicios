#Escreva um Progrma que leia em metros e o exiba convertido em centimetros e milimetros#

metros = float (input('Digite uma distãncia em metros: '))
centimetros = float (metros * 100)
milimetros =float (centimetros * 1000)

print(' O valor de {} em centimetros e de {} \n e em milinetros e igual a {}:'.format(metros,centimetros,milimetros))