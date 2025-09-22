n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Média: {media:.1f}')
if 5 < media <= 7:
    print('Aluno em RECUPERAÇÃO.')
elif media >= 7:
    print('Aluno APROVADO.')
else:
    print('Aluno REPROVADO.')