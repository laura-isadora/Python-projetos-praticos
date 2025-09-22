from datetime import date

atual = date.today().year
nascimento = int(input('Informe o ano de nascimento: '))
idade = atual - nascimento
print(f'IDADE: {idade}')

if idade <= 10:
    print('Classificação: MIRIM')
elif idade <= 15:
    print('Classificação: INFANTIL')
elif idade <= 20:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')