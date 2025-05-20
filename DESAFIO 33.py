#DESENVOLVA UM PROGRMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAEM EM KM
#CALCE O PREÇO DA PASSAGEM,COBRANDO R$0,50 PRO KM PARA VIAGENS DE ATE 200KM E R$0.45 PARA VIAGENS MAIS LONGAS

distancia = float(input('Digite a distância da sua viagem: '))
if distancia <= 200:
   preco = distancia * 0.50
else:
    preco = distancia *  0.45
print('Sua viagem vai custar R${:.2f}'.format(preco))
print('-=-' * 20)
