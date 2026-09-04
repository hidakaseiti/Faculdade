i = int(input('Digite um número de 0 a 10: '))
while i > 10 or i < 0:
    print('Valor inválido! Digite um número válido')
    break
i = int(input('Digite novamente: '))
if i <= 10 and i <= 10:
    print('Valor válido!')