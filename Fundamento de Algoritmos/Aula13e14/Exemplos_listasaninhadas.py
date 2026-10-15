#Recuperar uma lista dentro de uma lista como um elemento qualquer,só recuperar o indice do elemento
#recuperando um elemento da lista dentro da lista l[1][2] (elemento 1 da lista(uma lista)e elemento 2 da lista dentro da lista)
#Exemplo:crie 3 listas:uma com 5 numeros inteiros,outra com 3 numeros float,outra com 2 strings
#adicione cada uma dessas listas a uma nova lista vazia e imprima essa lista no final
##l1 = [1,2,3,4,5]
##l2 = [1.1,1.2,1.3]
##l3 = ['um','dois']
##l4 = []
##l4.append(l1)
##l4.append(l2)
##l4.append(l3)

#matriz: lista de listas
#por exemplo
# m = [[5,4,3], [2,8,6], [1,7,9]] (cada elemento(lista) é uma linha)
#recuperar linha 1: m[1] / recuperar linha 2: m[2] / recuperar elemento 0x0: m[0][0]
#recuperar elemento 1x1: m[1][1]

#Exemplo
##m = [[42, 7, 3], [9, 1, 6]]
##print(m[0][0] + m[0][1] + m[0][2] + m[1][0] + m[1][1] + m[1][2])

#imprimindo cada linha de uma matriz
#m = [[42,7,3], [9,1,6]]
#for i in range(len(m)):
#print(m[i])
#for l in m: (python- iterador)
#print(l)

#imprimir só os elementos de cada linha
##m = [[42, 7, 3], [9, 1, 6]]
##for l in m:
##  for x in l:
##      print(x, end=' ')
##  print()
##42 7 3
##9 1 6

#imprimir cada elemento da matriz
##m = [[42, 7, 3], [9, 1, 6]]
##for i in range(len(m)):
##   for j in range(len(m[i]))
##      print(m[i][j])
##42
##7
##3
##9
##1
##6

#imprimir cada elemento da matriz usando iterador
##m = [[42, 7, 3], [9, 1, 6]]
##for l in m:
##    for x in l:
##      print(x)

#Exemplo
##m = [[1,2,3], [4,5,6], [7,8,9]]
##acumulador = 0
##for l in m:
##    for x in l:
##        acumulador += x
##print(acumulador)
##m = [[1,2,3], [4,5,6], [7,8,9]]
##acumulador = 0
##for i in range(len(m)):
##    for x in range(len(m[i])):
##        acumulador += m[i][x]
##print(acumulador)

#Exemplo construindo uma matriz 3x3 e printando a soma de cada linha
##m = []
##for i in range(3):
##    l = []
##    for j in range(3):
##       l.append(i*3 + 1 + j) conta q o professor fez para obter 1,2,3;4,5,6;7,8,9
##    m.append(l)

##for l in m:
##    s = 0
##    for x in l:
##        s += x
##    print(s)

#Exemplo
##import random
##m = []
##for i in range(4):
##    l = []
##    for j in range(4):
##        l.append(random.randint(0, 9))
##    m.append(l)
##print(m)