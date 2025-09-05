# algoritimo para saber se o ano é bissexto
from datetime import date
ano = int(input('Qual ano você quer analisar? (Digite 0 para saber o ano atual) \n'))

# se o usuário digitar 'zero' o algoritmo mostrará o ano atual
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))
