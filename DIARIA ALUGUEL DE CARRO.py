
dias= int(input('Digite quantos dias alugados'))
distancia =float(input('Digite a distância Percorrida:'))
valor=(dias*60) + (distancia*0.15)


print('O valor a ser pago pela quantidade de dias {} é de R$: {:.2f}'.format(dias,valor))


