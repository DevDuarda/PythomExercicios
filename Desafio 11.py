largura= float (input('Digite a largura da Parede:'))
altura=float(input('Digite a altura da Parede:'))
area= largura*altura
print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m²'.format(largura,altura,area))
tinta= area/2
print('Para pintar essa parede,você vai precisar de {} Litros de Tinta :)'.format(tinta))
