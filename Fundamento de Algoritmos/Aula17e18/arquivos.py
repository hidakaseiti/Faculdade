#SINTAXE

# arquivo = open("teste.txt", "w")

#OPERACOES

#r leitura(read)
#w escrita(write)
#a escrita,preservando o conteúdo existente(append)
#+ atualização(combinando com r ou w)

#OBSERVACOES

#O write e parecido com print
#Depois de fazer as operacoes e importante fecha-lo utilizando o metodo close: arquivo.close()

#readline() le uma linha
#read le todas as linhas
#for l in f: le uma linha do arquivo a cada volta

#f = open('numeros.txt', 'w')
#for i in range(1,11):
#    f.write(f'{i}\n')    escreve em cada linha

#f = open('numeros.txt', 'r')
#ns = []
#for l in f:
#    x = l.rstrip() tira todos os espacos em branco do lado direito,caso contrario ele imprimiria \n
#    y = int(x) para converter para numeros mesmo,nao mais strings(essas duas linhas sao dispensaveis)
#    ns.append(y)
#print(ns)
#f.close()

##Exercicio 1
#f = open('pares.txt', 'w')
#s = open('impares.txt', 'w')

#for i in range(1000):
#    if i % 2 == 0:
#        f.write(f'{i},')
#    if i % 2 == 1:
#        s.write(f'{i},')
#f.close()
#s.close()

#Exercicio2
f = open('pares.txt', 'r')
p = open('multiplos4.txt', 'w')

for line in f: #nao da para retornar int para fazer conta pois esta tudo em uma linha só,desse jeito é preciso pegar esses numeros de algum jeito
    x = line.split(',') #retorna uma lista por isso,tem de iterar mais uma vez cada item da lista
    for i in x:
        m = int(i) 
        if m % 4 == 0:
            p.write(f'{i},') #da mais ou menos certo, no final, por causa do , ele esta separando por numa lista e tem um elemnto sem nada apos a virgula, portanto da erro ao dividir nada por 4
f.close()
p.close()

#jeito do professor
#pares = open('pares.txt', 'r')#
#with open('multiplos4.txt', 'w') as f: #cria um bloco e quando acabar automaticamente fecha
#    for line in pares:
#        x = int(line)
#        if x % 4 == 0:
#            f.write(f'{x}\n')
#pares.close()