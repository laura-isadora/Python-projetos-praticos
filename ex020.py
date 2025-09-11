num = int(input('Digite um número inteiro para conversão: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter pata HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é: {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é: {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é: {hex(num)[2:]}')
else:
    print('Opção inválida! Digite outro número.')