import random
nome1 =(input('Primeiro Nome:'))
nome2=(input('Segundo Nome:'))
nome3=(input('Terceiro Nome:'))
nome4=(input('Quarto Nome:'))
lista = [nome1,nome2,nome3,nome4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

