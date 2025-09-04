# solicitar a temperatura em °C
temp = float(input('Informe a temperatura em °C: '))

# conversão para fahrenheit
f = float(temp * 1.8) + 32

# mostrar o resultado
print('{} °C equivale a {} °F'.format(temp, f))
