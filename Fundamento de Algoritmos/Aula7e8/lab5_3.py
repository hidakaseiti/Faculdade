qtd = int(input('entre com a quantidade de numeros: '))
maior = 0
for i in range(1,qtd+1):
    numeros = int(input(f'número {i}: '))
    if i == 1:
        maior = numeros
    elif numeros > maior:
        maior = numeros
print(f'O maior número é {maior}')