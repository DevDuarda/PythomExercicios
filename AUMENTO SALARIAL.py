salario = float(input("Qual é o sálario do funcionário?"))
if salario <= 1250:
    novo = salario + (salario * 15/100)
    print('O sálario passa a ser {}'.format(novo))
else:
    novo = salario + (salario * 10/100)
    print('O sálario passa a ser {}'.format(novo))