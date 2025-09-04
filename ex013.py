from random import randint
from time import sleep

#solicitar que o usuário tente adivinhar o numero

print('Tente adivinhar o numero que estou pensando!\n')
numero = int(input('Em qual número eu pensei? '))

# mostrar ao usuário se ele acertou o numero que foi sorteado

print('PENSANDO...\n')
sleep(3)
computador = randint(0, 10)
if numero == computador:
    print('Parabéns! você acertou! Pensei no número {}'.format(computador))
else:
    print('Errou! o número que pensei é o {}'.format(computador))
