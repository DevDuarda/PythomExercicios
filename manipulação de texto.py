frase =str(input('Digite uma frase: '))
print('{}'[1:15]) #vai "fatiar" o texto
print('{}'.format(frase.count('b'))) #Contar quantas vezes a letra 'b' minuscula  aparece#
print('{}'.format(frase.find('luz'))) #Vai indicar a posição onde começa a sua busca#
print('{}'.format(len(frase))) # Conta quantos carecteres tem frase#
print('{}'.format('curso'in frase)) #Verifica se a palavra buscada, no caso:'Curso" esta dentro da sua frase#
print('{}'.format(frase.replace('eduarda','android'))) #Vai substituir,ex no lugar do nome eduarda, pedi para que ele tranforme em 'android'#
print('{}'.format(frase.upper())) #vai deixar as letras que antes estavem minusculo em maisculo#
print('{}'.format(frase.lower())) #Vai deixar as letras que estavem maisculas em minuculas#
print('{}'.format(frase.capitalize()))  #Todos os caracteres vao ficar em miusculo e somente a primeira letra vai ficar em maiusculo#
print('{}'.format(frase.title())) #Todas os caracteres de inicio de palavra vao ficar em mauisculo#
print('{}'.format(frase.strip()))#Vai remover todos os espaços inuteis#
print('{}'.format(frase.rstrip()))  #Remove somente os espaços do final
print('{}'.format(frase.lstrip())) #Remove somente os espaçoes do inicio"
print('{}'.format(frase.split())) #Vai dividir a sua frase apartir de cada espaço, ou seja apos cada espaço ele  'entende' como final da frase e 'inicia' outra frase
print('{}'.format('-'.join(frase))) #juntar todos as letras"



