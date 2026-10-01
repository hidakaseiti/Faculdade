valor = float(input('Digite o valor da compra: '))
parcelas = int(input('Digite a quantidade de parcelas: '))
if valor > 5000:
    if parcelas == 1:
        desconto = 0.15
    elif parcelas == 2 or parcelas == 3:
        desconto = 0.1
    elif parcelas > 3:
        desconto = 0.05
elif valor <= 5000:
    if parcelas == 1:
        desconto = 0.1
    elif parcelas == 2 or parcelas == 3:
        desconto = 0.05
    elif parcelas > 3:
        desconto = 0
print(f'Desconto total: {valor*desconto:.2f}')
print(f'Valor final da compra com desconto: {valor-valor*desconto:.2f}')
print(f'Cada parcela será de: {(valor-valor*desconto)/parcelas:.2f}')