n = int(input('Coloque um número: '))
for i in range(n):
    for j in range(1,i+2,1):
        print(j, end= ' ')
    print()
for i in range(n+1):
    for j in range(i+1):
        print(j, end= ' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(j+1, end=' ')
    