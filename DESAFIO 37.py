#DESENVOLVA UM PROGRAMA QUE ELIA O COMPRIMENTO DE TRÊS RETAS E FIGA AO USARIO SE ELAS PODEM OU NÃO FORMAR UM TRIANGULO
print('--__--'*20)
print("ANALISADOR DE TRIÂNGULO")
print('--__--'*20)
n1= float(input('\033[0;30;41m Digite o primeiro segmento;'))
n2= float(input('\033[4;33;44m Digite o segundo segmento;'))
n3= float(input('\033[30;42m Digite o terceiro segmento;'))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[30;40m segmentos acima PODEM FORMAR UM TRIÂNGULO')
else:
    print('\033[4;30mOs segmento acima NÃO PODEM FORMAR UM TRIÂNGULO\033[m')
