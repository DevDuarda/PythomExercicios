#CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É PAR OU IMPAR

n1= int(input('Digite um número:'))
if n1 % 2 == 0: #RESTO DA DIVISÃO DESSE NÚMERO POR 2
    print('Seu numero {} é par!'.format(n1))
else:
    print('Seu número {} é impar!'.format(n1))

print('-=-' * 20)
print('FIM')