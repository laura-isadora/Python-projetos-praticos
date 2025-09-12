from datetime import date
print('=' * 36)
print('\033[32mPROGRAMA DE ALISTAMENTO DO EXERCITO\033[m')
print('=' * 36)

# ano atual
atual = date.today().year
#ano de nascimento
nasc = int(input('\nAno de nascimento: '))
sexo = str(input('Sexo: '))
# idade será o ano atual - o ano de nascimento
idade = atual - nasc

# verificar quando será o alistamento
if idade == 18 and sexo.lower() == 'masculino':
    print(f'Idade: {idade}')
    print('Você deve se alistar IMEDIATAMENTE.')
elif idade < 18 and sexo.lower() == 'masculino':
    diferenca = 18 - idade
    ano = atual + diferenca
    print(f'Idade: {idade}')
    print(f'Ano de alistamento: {ano}')
    print(f'Faltam {diferenca} anos para o seu alistamento.')
elif idade > 18 and sexo.lower() == 'masculino':
    diferenca = idade - 18
    ano = atual - diferenca
    print(f'Idade: {idade}')
    print(f'Ano de alistamento: {ano}')
    print(f'Seu alistamento foi há {diferenca} anos.')
else:
    print('Você não tem obrigatoriedade de alistamento.')