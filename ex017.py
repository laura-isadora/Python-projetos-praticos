print('\033[35m-\033[m' * 23)
print('\033[4;35mANALISANDO TRIÂNGULOS\033[m')
print('\033[35m-\033[m' * 23)

# solicitar as medidas das retas ao usuário
r1 = float(input('\nDigite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

# calculo para saber se pode ser formado um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
     # três retas iguais formam um triângulo equilátero
    if r1 == r2 == r3:
        print('Esses segmentos formam um triângulo EQUILÁTERO!')
    # duas retas iguais e uma diferente formam um triângulo isósceles
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esses segmentos formam um triângulo ISÓSCELES!')
    # todas as retas com comprimentos diferentes formam um triângulo escaleno
    else:
        print('Esses segmentos formam um triângulo ESCALENO!')
else:
    print('Esses segmentos NÃO podem formar um triângulo!')

