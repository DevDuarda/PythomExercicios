#Crie um algoritmo que leia um número e mostre o seu dobro,triplo e raiz quadrada#
n = int (input('Digite um número'))
d = n*2
t = n*3
r = n**(1/2)

print('O dobro de {} é igual a {}'.format(n,d))
print('O Triplo de {} é igual a {}'.format(n,t))
print('A raiz quadra de {} é igual a {:.2f}'.format(n,r))

