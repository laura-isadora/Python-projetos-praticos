# solicitar o peso para calculo do IMC
print('Vamos calcular seu IMC?\n')
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))

# calculo do IMC:
imc = peso / (altura ** 2)

# mostrar o IMC e o Status do peso
if imc < 18.5:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Classificação: Abaixo do peso!')
elif 18.5 <= imc < 24.9:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Classificação: Peso normal!')
elif 25 <= imc < 29.9:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Classificação: Sobrepeso!')
elif 30 <= imc < 34.9:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Classificação: \033[31mOBESIDADE GRAU I\033[m')
elif 35 <= imc < 39.9:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Classificação: \033[31mOBESIDADE GRAU II\033[m')
else:
    print('Seu IMC é: {:.2f}'.format(imc))
    print('Classificação: \033[31mOBESIDADE GRAU III\033[m')