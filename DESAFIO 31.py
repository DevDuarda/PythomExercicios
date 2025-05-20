#ESCREVA UM PROGRAMA QUE LEUA A VELOCIDADE DE UM CARRO
#SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
# A MULTA VAI CUSTAR R$ 7.00 POR KM ACIMA DO LIMITE

velocidade = float(input('Qual a velocidade atual do carro?'))

if velocidade >80:
    print('MULTADO,Você excedeu o limite permitido, que é de 80KM/H Você deve pagar uma multa no valor  de R$: {:.2f}!'.format(velocidade))
    multa = (velocidade -80)*7

print('Tenha um bom dia, dirija com segurança...')