# solicitar o valor da compra
valor = float(input('Informe o valor da sua compra: '))

# calcular o desconto
porcentagem = float(valor / 100) * 5
desconto = valor - porcentagem

#mostrar o valor final com o desconto
print('O valor com desconto é : R${:.2f}'.format(desconto))
