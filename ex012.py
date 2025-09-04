n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é: {:.1f}'.format(media))
if media >= 7:
    print('Parabéns, sua média é boa!')
else:
    print('Sua média esta ruim!')