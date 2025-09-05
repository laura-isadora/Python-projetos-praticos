# calculo de aumento de salário
salario = float(input('Informe o valor do salário: '))

# calculo para salarios maiores que R$1.250,00
if salario > 1250:
    aumento = (salario * 0.10) + salario
    print('Aumento de 10%!')
# calculo para salarios menores ou iguais a R$1.250,00
else:
    aumento = (salario * 0.15) + salario
    print('Aumento de 15%!')

print('Salário atual: {}'.format(aumento))