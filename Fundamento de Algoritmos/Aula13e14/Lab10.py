#Exercicio 1
##import math
##m = []
##maior = -math.inf
##for i in range(2):
##    l = []
##    for j in range(2):
##        x = int(input(f'Digite o elemento da linha {i} e coluna {j}: '))
##        l.append(x)
##        if x > maior:
##            maior = x
##    m.append(l)
##k = []
##print('Matriz resultante: ')
##for j in m:
##    l = []
##    for n in j:
##        l.append(n*maior)
##        print(f' {n*maior}', end=' ')
##    print()
##    k.append(l)

#Exercicio 2
##t = int(input('Digite a ordem da matriz: '))
##m = []
##for i in range(t):
##  l = []
##  for j in range(t):
##      l.append(2**(i+j))
##      print(f' {2**(i+j)}', end= ' ')
##  print()
##  m.append(l)