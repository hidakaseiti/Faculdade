#python string methods
#string: sequencia de caracteres,a representacao de um caractere é dada por um numero inteiro,hexadecimal ou binario
#o python usa unicode

#exemplo de metodos: capitalize(), count(), find(), lower(), islower(), isdigit(), isalpha(), split(), strip(), replace()

#LABORATORIO 12
#Exercicio 1
#def conc(s1,s2):
#    s3 = s1 + s2
#    return s3

#Exercicio 2
#def conc_com_espacos(s1, s2, s3):
#    s4 = s1 + ' ' + s2 + ' ' + s3
#    return s4

#Exercicio 3
#def sem_espacos(string):
#    s = string.strip()
#    return s

#Exercicio 4
#def contar(s):
#    string = len(s)
#    return string

#Exercicio 5
#def cm(s):
#    a = 0
#    for letra in s:
#        if letra.isupper() == True:
#            a += 1
#    return a

#Exercicio 6
#def inv(string):
#    s = ''
#    for letra in string:
#        if letra.isupper() == True:
#            letra = letra.lower()
#            s += letra
#        elif letra.islower() == True:
#            letra = letra.upper()
#            s += letra
#    return s

#Exercicio 7
#def longest(s1,s2):
#    contador = len(s1)
#    contador2 = len(s2)
#    if contador >= contador2:
#        return s1
#    elif contador2 > contador:
#        return s2

#Exercicio 8
#def separa(string):
#    a = string.split(',')
#    return lista

#Exercicio 9
#def separar(string):
#    a = string.split(',')
#    lista = []
#    for elemento in a:
#        b = elemento.strip()
#        lista.append(b)
#    return lista