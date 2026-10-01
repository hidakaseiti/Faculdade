N = int(input('Digite o número desejado: '))
E = 1
for i in range(1,N+1):
    E += 1/i
print(f'{E:.3f}')