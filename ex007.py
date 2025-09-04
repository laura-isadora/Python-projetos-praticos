# solicitar o valor inicial do salário de um funcionário
salario = float(input('Informe o salário: '))

# calculo da porcentagem e acrescimo no salário
porcentagem = float(salario / 100) * 15
acrescimo = salario + porcentagem

# mostrar o valor final com o acrescimo
print('O salário com o aumento de 15% é: {:.2f}'.format(acrescimo))
