n = int(input('Coloque um número: '))
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print() 
for i in range(n):
    for j in range(n-i):
        print('*', end=' ')
    print()