#def procura_chave(dicionario, valor):
#    l = []
#    for chave in dicionario:
#        if dicionario[chave] == valor:
#            l.append(chave)
#    return l
#d = {'foo':1, 'bar':7, 'bar':1}
#l = procura_chave(d,1)
#print(l)

#def procura_chave(dicionario, valor):
#    l = []
#    for k,v in dicionario.items():
#        if v == valor:
#            l.append(k)
#    return l
#d = {'foo':1, 'bar':7, 'baz':1}
#l = procura_chave(d,7)
#print(l)

#jeito que o professor fez:
#def procura_chave(dicionario, x):
#    return [k for k,v in dicionario.items() if v == x] esse metodo chama LIST COMPREHENSION

#def count(lista):
#    dicionario = {}
#    for i in range(len(lista)):
#        if dicionario[lista[i]] in dicionario:
#            dicionario[lista[i]] += 1
#        else:
#            dicionario[lista[i]] = 1
#    return dicionario

#exercicio 3 prof que fez
#def is_anagram(palavra1, palavra2):
#    d1 = {}
#    for letra in palavra1:
#        d1[letra] = 1 + d1.get(letra, 0)
#    d2 = {}
#    for letra in palavra2:
#        if letra in d2:
#            d2[letra] += 1
#        else:
#            d2[letra] = 1
#            return d1 == d2

#apelando
#def is_anagram(palavra1, palavra2):
#    p1 = sorted(palavra1)
#    p2 = sorted(palavra2)
#    return p1 == p2

#def uniq(string):
#    dicionario = {}
#    for letra in string:
#        dicionario[letra] = 1
#    letras_distintas = 0
#    for distinta in dicionario.values():
#        letra_distintas += 1
#    return letras_distintas