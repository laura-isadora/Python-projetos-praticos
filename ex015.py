a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

# verificar qual numero é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# verificar qual número é maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor número é o {}'.format(menor))
print('O maior número é o {}'.format(maior))
