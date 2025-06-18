n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print ( 'a sua média foi {:.1f}'.format(m))
if m >=7.0:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')
