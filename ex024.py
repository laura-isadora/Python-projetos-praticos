print('-'*20)
print('SISTEMA DE PAGAMENTO')
print('-'*20)
print('''\n[1] Dinheiro/Pix
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('\nEscolha uma opção de pagamento: '))
compra = float(input('Informe o valor da compra: R$'))

# dinheiro/Pix: 10% de desconto
if opcao == 1:
    desconto = compra * 0.90
    print('Desconto de 10%')
    print(f'VALOR FINAL: R${desconto:.2f}')

# à vista no cartão: 5% de desconto
elif opcao == 2:
    desconto = compra * 0.95
    print('Desconto de 5%')
    print(f'VALOR FINAL: R${desconto:.2f}')

# em até 2x no cartão: preço normal
elif opcao == 3:
    print(f'1x de R${compra:.2f}')
    print(f'2x de R${compra/2:.2f}')
    print(f'VALOR FINAL: R${compra:.2f}')

# 3x ou mais no cartão: 20% de juros
elif opcao == 4:
    parcelas = int(input('Quantidade de parcelas: '))
    total = compra * 1.20
    parcelamento = total / parcelas
    print(f'{parcelas}x de R${parcelamento:.2f}')
    print(f'VALOR FINAL: R${total:.2f}')

else:
    print("Opção inválida! Tente novamente.")
