import math as m #math é o módulo com várias funções
import random as r #random é o módulo com várias funções
#from random import sample #importa a função direto,ou seja da para escrever só sample
#from math import * #importa todas as funções (não é recomendado)

#procurar no docs python para ver todos os modulos e funções

print(m.sqrt(9)) #raiz quadrada
print(r.randint(7,42)) #número aleatório inteiro
print(r.sample([5,8,9],1)) #1 é o tamanho da amostra

######criando a própria biblioteca
#def media(l):
#    c = 0
#    for x in l: #recorto a funcão e colo na matematica.py que vai virar a biblioteca/modulo
#        c += x
#        return c/len(l)

import matematica
from matematica import media

l = [4,5,6,3,2,1,3]
print(matematica.media(l))
l2 = [3,1,2,3,4]
print(matematica.soma(l2))