# aluguel de carros
dias = int(input('Quantidade de dias: '))
km = float(input('Quantos kms percorridos: '))

# calculo para saber o valor que deve ser pago
# R$60,00 por dia e R$0,15 por km
valor_dias = float(dias * 60)
valor_km = float(km * 0.15)
total = valor_dias + valor_km

# mostrar o valor final
print('O valor a ser pago é: {}'.format(total))
