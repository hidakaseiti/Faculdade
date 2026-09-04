idade= int(input("Sua idade:"))
if idade>=1 and idade<=12:
    print("Classificação:criança")
elif idade>12 and idade<=18:
    print("Classificação:adolescente")
elif idade>18 and idade<=65:
    print("Classificação:adulto")
else:
    print("Classficiação:idoso")