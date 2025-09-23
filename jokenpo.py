# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from colorama import Fore, Back, Style, init
import time

init(autoreset=True)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)

print(Fore.LIGHTWHITE_EX + Style.BRIGHT + '''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input(Fore.WHITE + Style.BRIGHT + '\nQual é a sua jogada? '))

print(Fore.LIGHTBLUE_EX + Style.BRIGHT + '\nJO')
time.sleep(1)
print(Fore.LIGHTBLUE_EX + Style.BRIGHT +  'KEN')
time.sleep(1)
print(Fore.LIGHTBLUE_EX + Style.BRIGHT + 'PÔ')

print(Fore.MAGENTA + Style.BRIGHT + '-=-'*8)
print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f'Computador jogou {itens[computador]}')
print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f'Jogador jogou {itens[jogador]}')
print(Fore.MAGENTA + Style.BRIGHT + '-=-'*8)

if computador == 0: # computador jogou pedra
    if jogador == 0: # jogador jogou pedra
        print(Fore.YELLOW + Style.BRIGHT + 'EMPATE!')
    elif jogador == 1: # jogador jogou papel
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + 'VOCÊ VENCEU!')
    elif jogador == 2: # jogador jogou tesoura
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + 'COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
elif computador == 1: # computador jogou papel
    if jogador == 0: # jogador jogou pedra
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + 'COMPUTADOR VENCEU!')
    elif jogador  == 1: # jogador jogou papel
        print(Fore.YELLOW + Style.BRIGHT + 'EMPATE!')
    elif jogador == 2: # jogador jogou tesoura
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + 'VOCÊ VENCEU!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
elif computador == 2: # computador jogou tesoura
    if jogador == 0: # jogador jogou pedra
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + 'VOCÊ VENCEU!')
    elif jogador == 1: # jogador jogou papel
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT + 'COMPUTADOR VENCEU!')
    elif jogador == 2: # jogador jogou tesoura
        print(Fore.YELLOW + Style.BRIGHT + 'EMPATE!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
