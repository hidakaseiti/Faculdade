numero_casos = int(input())
animais = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(numero_casos):
    quantidade = int(input())
    tipo = input()

    animais += quantidade

    if tipo == 'C':
        coelhos += quantidade
    elif tipo == 'R':
        ratos += quantidade
    elif tipo == 'S':
        sapos += quantidade

print(f'Total: {animais} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')

print(f'Percentual de coelhos: {(coelhos / animais) * 100:.2f} %')
print(f'Percentual de ratos: {(ratos / animais) * 100:.2f} %')
print(f'Percentual de sapos: {(sapos / animais) * 100:.2f} %')
