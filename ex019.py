print('-' * 25)
print('EMPRÉSTIMO BANCÁRIO')
print('-' * 25)

#solicitar os dados para o usuário
valor = float(input('\nValor do imóvel: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = int(input('Tempo de financiamento (anos): '))

# calculo da prestação mensal
prestacao = valor / (tempo * 12)
print(f'\nA prestação será de {prestacao:.2f}')

# verificação do limite de 30% do salário
if prestacao > (salario * 0.30):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO CONCEDIDO!')
