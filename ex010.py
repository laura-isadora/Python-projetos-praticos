from random import choice
#solicitar o nome dos participantes para sortear
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]

#criar a variável para sortear um nome aleatório com base na lista que foi criada
escolhido = choice(lista)
print('\nO nome escolhido foi: {}'.format(escolhido))
