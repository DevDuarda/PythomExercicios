nome=str(input('Digite seu nome completo:')).strip()
print('Seu nome em maiúsculo é:{}'.format(nome.upper()))
print('Seu nome em minúsculo é:{}'.format(nome.lower()))
print('Seu Nome tem a todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome,nome.find(' ')))




