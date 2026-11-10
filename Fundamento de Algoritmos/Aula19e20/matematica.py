#essa pasta é um modulo para ser usado em qualquer programa importando para ele

def media(l):
    c = 0
    for x in l:
        c += x
        return c/len(l)

###da para fazer assim tambem,e nao da problema no return soma(l) mesmo estando depois,pq ele nao esta sendo executado dentro da funcao
#def media(l):
#    c = 0
#    for x in l:
#        c += x
#        return soma(l)/len(l)

def soma(l):
    c = 0
    for x in l:
        c += x
        return c
