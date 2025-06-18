'''Listas:

Parte Teorica:
O que são:
Uma coleção mutável de elementos, ou seja: você pode alterar (adicionar, remover, modificar os itens).

Características:
Aceitam diferentes tipos de dados

Podem crescer ou diminuir de tamanho

Usam colchetes [ ]
Exemplos de lista:
'''
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")   # Adiciona
frutas[0] = "abacaxi"       # Modifica
print(frutas)               # Resultado: ['abacaxi', 'banana', 'uva', 'laranja']


'''Tuplas em Python (tuple)
O que são:
Uma coleção imutável de elementos, ou seja: não pode mudar depois de criada.

Características:
Mais rápida que lista

Usada quando você quer proteger os dados contra alterações

Usa parênteses ( )'''

cores = ("vermelho", "verde", "azul")
print(cores[1])   # Resultado: verde
# cores[0] = "amarelo"  # Isso vai dar erro! (imutável)

'''
| Característica | Lista                       | Tupla                                  |
| -------------- | --------------------------- | -------------------------------------- |
| Mutável?       | Sim                         | Não                                    |
| Símbolo        | `[ ]`                       | `( )`                                  |
| Performance    | Mais lenta                  | Mais rápida                            |
| Quando usar    | Quando os dados podem mudar | Quando os dados devem permanecer fixos |
'''