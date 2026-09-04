Valor = float(input('Valor da compra: '))
Parcelas = int(input('Número de parcelas: '))

if Valor > 5000:
    Valor = Valor*0.95
    print('O desconto é de ')
    if Parcelas == 1:
        Valor = Valor*0.9
    elif Parcelas == 2 or 3:
        Valor = Valor*0.95
        print('O valor final é de ')
elif Valor < 5000:
    if Parcelas == 1:
        Valor = Valor*0.9
    elif Parcelas == 2 or 3:
        Valor = Valor*0.95
        print('O valor final é de ')