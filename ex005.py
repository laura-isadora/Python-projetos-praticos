# solicitar os dados para o usuário (considerando o valor do dólar a R$3,27)
valor = float(input('Informe a quantidade em Reais: '))

# calculo da conversão para dólares
cotacao = 3.27
dolares = float(valor / cotacao)

# mostrar quantos dólares é possível comprar
print('Você pode comprar {:.2f} dólares'.format(dolares))
