#declarar as variáveis
altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

#fazer o calculo de altura x largura
area = float(altura * largura)

#fazer o calculo de quantidade de tinta
tinta = float(area/2)

# mostrar a área e o resultado
print('Área: {:.2f}m²'.format(area))
print('A quantidade de tinta que será utilizada será de {:.2f} litros'.format(tinta))