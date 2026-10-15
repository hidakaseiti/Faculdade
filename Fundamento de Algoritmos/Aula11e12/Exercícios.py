#Exercício 1:
##l = []
##for i in range(5):
##    v = int(input('Digite um valor: '))
##    l.append(v)
##print(l, l[0], l[4])

#Exercício 2:
##import math
##def menor(l):
##    a = math.inf
##    for x in l:
##        if x < a:
##            a = x
##    return a

#Exercício 3:
##import math
##def maior(l):
##    a = -math.inf
##    for x in l:
##        if x > a:
##            a = x
##    return a

#Exercício 4:
##l = []
##a = 0
##i = 0
##for x in range(10):
##    n = float(input('Digite um número real: '))
##    l.append(n)
##    if n > a:
##        a = n
##        i = x
##print(a, i)

#Exercício 5:
##def pares(l):
##    a = 0
##    for i in range(len(l)):
##        if l[i] % 2 == 0:
##            a += l[i]
##    return a

#Exercício 6:
##def ímpares(l):
##    a = 0
##    for i in range(len(l)):
##        if l[i] % 2 == 1:
##            a += l[i]
##    return a

#Exercício 7:
##def inversa(l):
##    l2 = []
##    for i in range(len(l) - 1,-1,-1):
##        l2.append(l(i))
##    return l2

#Exercício 8:
##def anteriores(l):
##    l2 = []
##    for i in range(len(l)):
##        if l[i] > l[i-1] + l[i-2]:
##            l2.append(l[i])
##    return l2

##l = [2, 6, 20, 56]para testar
##m = anteriores(l)
##print(m)

#Exercício 9
##def temp(l):
##    import math
##    maxima = -math.inf
##    minima = math.inf
##    soma = 0
##    for x in l:
##        soma += x
##        if x > maxima:
##            maxima = x
##        if x < minima:
##            minima = x
##    media = soma/len(l)
##    return maxima, minima, media

##l = [20, 25, 23, 28, 30]
##k = temp(l)
##print(k)

#Exercício 10
##def comum(l1,l2):
##    l3 = []
##    for a in l1:
##        for b in l2:
##            if a == b:
##                l3.append(a)
##    return l3
##l1 = [2, 3, 5, 7, 11, 13, 17]
##l2 = [1, 4, 5, 6, 12, 13, 17, 30, 50]
##k = comum(l1,l2)
##print(k)

#Exercício 11
##def uniao(l1, l2):
##    l3 = []
##    for a in range(len(l1)):
##        l3.append(l1[a])
##    for b in range(len(l2)):
##        l3.append(l2[b])
##    return l3

#Exercício 12
##def diferenca(l1, l2):
##    l3 = []
##    for a in l1:
##        if a not in l2:
##            l3.append(a)
##    for b in l2:
##        if b not in l1:
##            l3.append(b)
##    return l3
##l1 = [1,2,3,4,5]
##l2 = [1,6,2,7,3,8,4,9,5,10]
##k = diferenca(l1, l2)
##print(k)

#Exercício 13
##def unicos(l1):
##    l2 = []
##    for a in range(len(l1)):
##        for b in range(len(l1)):
##            if l1[a] == l1[b]:
##                l2.append(a)
##    return l2
##l1 = [1,1,2,3,3,4,5,5,6,7,7]
##k = unicos(l1)
##print(k)

#Exercício 14
def segundo(l):
    import math
    m = -math.inf
    seg = -math.inf
    for x in l:
        if x > m:
            seg = m
            m = x
        elif x > seg:
            seg = x
    return seg

l = [1,2,3,4,5,6]            
k = segundo(l)
print(k)
