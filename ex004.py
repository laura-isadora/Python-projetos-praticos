# exibir as instruções e solicitar os números
print('Digite o valor em metros para converter em centímetros e milímetros e quilômetros.')
metros = float(input('Digite o valor em metros: '))

# calculo para conversão em centímetros e milímetros
centimetros = float(metros * 100)
milimetros = float(metros * 1000)
quilometros = float(metros / 1000)

# imprimir na tela os valores
print('{} metros equivalem a {:.2f} centímetros, {:.2f} milímetros e {:.2f} quilômetros.'.format(metros, centimetros, milimetros, quilometros))
