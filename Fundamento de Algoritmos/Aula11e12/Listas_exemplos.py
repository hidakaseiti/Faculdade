# Lista armazenada numa variável
##l = ['bolos',3,'café',42.7]

#Os itens da lista estão localizados em índices: números inteiros,primeiro item no índice 0;segundo no índice 2...
#Para recuperar um item: l[1] (recupera o elemento localizado no índice 1)
#Exemplo: l[1] + l[3] vai dar 45.7,recupera os itens e soma

##print(f'Eu comi {l[1]} {l[0]} e tomei {l[3]} litros de {l[2]}')

#Para alterar o valor de um elemento da lista: l[0] = 42 (por exemplo)

#A função len retorna o tamanho da lista: len([3,4,89,1,3]) retorna 5
#Usando índices,for e range dá para imprimir os itens da lista
#l = [958, 38, 13]
#for i in range(len(l)):  no range do tamanho da lista de l,ou seja: for i in range(3)
    #print(l[i])          printa l[0],l[1] e l[2]
#958
#38
#13

##l = [2,3,5,7,11]
##for i in range(len(l)):
##    l[i] /= 2
##print(l)

#É possível iter pelos itens da lista diretamente
#l = [94, 33, 3, 13 ,76]
#for x in l:
#    print(x)
#94
#33
#3
#12
#76

##l = [8, 45, 3, 12]
##for i in range(len(l)):
##    print(l[i]*2)
#prof fez assim (só do phyton esse for x in l:)
##l = [8, 42, 3, 12]
##for x in l:
##    print(x*2)

##l = [9, 8, 7, 6]
##a = 0
##for i in range(len(l)):
##    a += l[i]
##print(a)
#ou
##l = [9, 8, 7, 6]
##a = 0
##for x in l:
##    a += x
##print(a)

#O método append adiciona um item à lista, que é uma função da lista
#l = []
#l.append(42)
#print(l)
#42
#l.append(7)
#l.append(3)
#l.append('foo')
#print(l)
#42, 7, 3, foo

##l = [1, 2, 3, 4]
##l2 = []
##for x in l:
##    l2.append(x*2)
##print(l2)

#O método pop retira um item da lista através da índice
#l = [5, 4, 3, 2]
#l.pop(0)
#print(l)
#4, 3, 2
#l.pop()
#print(l)
#4, 3

#O método remove retira um item da lista por igualdade(retira o valor,não o índice)
#l = [8, 3, 4, 6, 4, 8]
#l.remove(3)
#l.remove(8) remove o primeiro encontrado
#print(l)
#4, 6, 4, 8

#Operador in retorna True se item está na lista
#l = ['foo', 42, 'bar']
#'foo'in l
#True
#if 42 in l:
#   print('Está na lista!')
#Está na lista!

# : dentro de colchetes fatia uma lista
#l = ['foo', 'bar', 'baz']
#l[0:2] pega foo e bar
#l[1:3] pega bar e baz
#l[:2] pega desde o inicio da lista
#l[0:] pega até o fim da lista
#l[:] pega do ínicio ao fim

#O operador + concatena duas listas
#l = [1, 3] + [2, 4]
#l = [1,3,2,4] só junta,não colocar na ordem nem nada

#O método extend extende e altera a lista original
#l = []
#l.extend([3,3])
#print(l)
#3, 3

#abrir Jupyter pelo google colab ou local no pc