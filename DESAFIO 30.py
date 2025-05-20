#ESCREVA UM PROGRAMA QUE FAÇA UM COMPUTADOR  'PENSAR' EM UM NÚMERO INTEIRO ENTRE 0 E 5
#E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL DOI O NÚMERO ESCOLHIDO PELO COMPUTADOR
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUARIO VENCEU OU PERDEU

from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "Pensar em um numero"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei?')) #JOGADOR TENTA ADIVINHAR
print('PROCESSANDO...')
sleep(3)
if jogador == computador: #RESPOSTA SE O JOGADOR PENSAR NO MESMO NÚMERO QUE O PROGRAMA
    print('Parabéns você ganhou !! ')
else: #SE O JOGADOR NÃO PENSAR NO MESMO NÚMERO
    print('Você perdeu, eu pensei no número {} e não  no {}'.format(computador, jogador))
print('-=-' * 20)


