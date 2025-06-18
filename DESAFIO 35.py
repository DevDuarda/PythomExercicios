salario = float(input('Qual é o salário do funcionário R$?'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print('O valor da sálario passar a ser {:.2f} '.format(novo))
else:
   novo= salario + (salario * 10 / 100)
   print('O valor do sálario passar a ser {:.2f} '.format(novo))