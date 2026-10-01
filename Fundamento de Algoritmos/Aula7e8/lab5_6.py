ano = int(input('Digite o ano desejado: '))

salario = 5000
aumento = 1.5

for i in range(2006, ano + 1):
    salario += salario * aumento / 100
    aumento *= 2

print(f'Salário de {ano}: R$ {salario:.2f}')