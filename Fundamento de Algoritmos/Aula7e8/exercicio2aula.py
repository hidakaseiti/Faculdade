L = int(input('Digite o tamanho do lado L,maior que 0: '))
C = int(input('Digite o tamnho do lado C,maior que 0: '))
for i in range(L):
    for j in range(C):
        if j == 0 or j == C - 1 or i == 0 or i == L - 1:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()