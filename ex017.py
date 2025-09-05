print('-' * 23)
print('ANALISANDO TRIÂNGULOS')
print('-' * 23)

# solicitar as medidas das retas ao usuário
r1 = float(input('\nDigite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

# calculo para saber se pode ser formado um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Esses segmentos formam um triângulo!')
else:
    print('Esses segmentos NÃO podem formar um triângulo!')