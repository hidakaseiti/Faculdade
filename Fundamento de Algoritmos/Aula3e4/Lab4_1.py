class1= input('Primeira palavra: ')
class2= input('Segunda palavra: ')
class3= input('Terceira palavra: ')
if class1=='invertebrado':
    if class2=='inseto':
        if class3=='hematofago':
            print('pulga')
        elif class3=='herbivoro':
            print('lagarta')
if class1=='invertebrado':
    if class2=='anelideo':
        if class3=='hematofago':
            print('sanguessuga')
        elif class3=='onivoro':
            print('minhoca')
if class1=='vertebrado':
    if class2=='mamifero':
        if class3=='herbivoro':
            print('vaca')
        elif class3=='onivoro':
            print('homem')
if class1=='vertebrado':
    if class2=='ave':
        if class3=='carnivoro':
            print('aguia')
        elif class3=='onivoro':
            print('pomba')