n = int(input('Digite a quantidade de números a serem testados: '))
a = 0
for i in range(1,n+1):
    x = int(input(f'Digite o número {i}:'))
    if x >= 2:
        for j in range(2,x):
            if x%j == 0:
                break
        else:
            a += 1
print(f'Você digitou {a} números primos')